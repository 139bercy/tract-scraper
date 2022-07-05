import scrapy
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError
from scraper.utils.fileUtils import to_html_filename, to_filename, in_downloads
from scraper.utils.urlUtils import clean_url
from urllib.parse import urljoin
from scrapy.utils.project import get_project_settings
import logging

settings = get_project_settings()

logger = logging.getLogger(__name__)


class BaseSpider(scrapy.Spider):
    
    name = None
    
    article_selector_in_list = None
    article_title_selector_in_list = None
    article_link_selector_in_list = None
    article_date_selector_in_list = None
    article_date_format_in_list = None
    article_date_separator_in_list = None
    article_date_term_in_list = None
    article_count = 0

    article_html_selector = None
    article_file_selector = None

    page_index = None
    page_offset = None
    page_offset_step = None
    page_selector = None

    start_urls = []

    def parse_article_date(self, container):
        date = None
        if isinstance(self.article_date_selector_in_list, list):
            date_parts = []
            for date_selector in self.article_date_selector_in_list:
                date_part = container.css(date_selector).get().strip()
                if date_part is not None and self.article_date_term_in_list is not None:
                    for term in self.article_date_term_in_list:
                        date_part = date_part.replace(term, self.article_date_term_in_list[term]) 
                date_parts.append(date_part)
            date = ' '.join(date_parts)
        else:
            date = container.css(self.article_date_selector_in_list).get()
            if date is not None and self.article_date_term_in_list is not None:
                for term in self.article_date_term_in_list:
                    date = date.replace(term, self.article_date_term_in_list[term])

        if date is None or date.isspace():
            return None

        date_str = str(date.encode('utf-8').decode('utf-8')).strip()
        if self.article_date_separator_in_list is not None:
            date_str = date_str.split(self.article_date_separator_in_list)[-1].strip()
        return datetime.strptime(date_str, self.article_date_format_in_list).date()

    def parse_article_url_in_list(self, response, container):
        url = container.css(self.article_link_selector_in_list).get()
        return response.urljoin(str(url)).strip()

    def handle_error(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    def parse_article(self, response):
        article = response.css(self.article_html_selector)
        article_title = response.meta['article_title']
        article_date = response.meta['article_date']
        
        file_name = to_html_filename(self.name, article_date, article_title)
        file_content = article.get()
        if not in_downloads(file_name):
            yield {
                    'type': 'html',
                    'file_name': file_name,
                    'file_content': file_content
                }

        if self.article_file_selector is None:
            return None

        file_relative_urls = article.css(self.article_file_selector).getall()
        for file_relative_url in file_relative_urls:
            file_name = to_filename(self.name, article_date, article_title, file_relative_url)
            if file_relative_urls and not in_downloads(file_name):
                yield {
                    'type': 'file',
                    'file_name': file_name,
                    'file_url': response.urljoin(file_relative_url)
                }
        self.logger.info(file_name)

    def parse(self, response):
        containers = response.css(self.article_selector_in_list)
        logger.info('Found %d articles in %s', len(containers), response.url)
        missing_date = 0
        article_date = date.today()
        min_date = article_date - relativedelta(weeks=settings.get('WEEKS_TO_SCRAP'))
        for container in containers:
            article_date = self.parse_article_date(container)
            if article_date is None or article_date <= min_date:
                missing_date += 1
                continue
            article_title = container.css(self.article_title_selector_in_list).get()
            article_meta = {
                'article_title': article_title,
                'article_date': article_date
            }

            if self.article_link_selector_in_list is None:
                file_name = to_html_filename(self.name, article_date, article_title)
                file_content = container.get()
                if not in_downloads(file_name):
                    yield {
                        'type': 'html',
                        'file_name': file_name,
                        'file_content': file_content
                    }

                if self.article_file_selector is None:
                    logger.info('No file selector for %s', response.url)
                    return None

                file_relative_urls = container.css(self.article_file_selector).getall()
                for file_relative_url in file_relative_urls:
                    file_name = to_filename(self.name, article_date, article_title, file_relative_url)
                    if file_relative_urls and not in_downloads(file_name):
                        yield {
                            'type': 'file',
                            'file_name': file_name,
                            'file_url': response.urljoin(file_relative_url)
                        }
            else:
                article_url = self.parse_article_url_in_list(response, container)
                yield scrapy.Request(url=article_url, callback=self.parse_article, errback=self.handle_error, meta=article_meta)

        if missing_date > 0:
            logger.info('%d articles not scraped because of date missing', missing_date)

        if article_date is not None and article_date > min_date:
            next_url = None
            if self.page_index is not None:
                self.page_index += 1
                if self.page_index >= 10:
                    return
                next_url = urljoin(clean_url(response.url), self.page_selector.format(page = self.page_index))
            elif self.page_offset is not None:
                self.page_offset += self.page_limit
                if self.page_offset >= 100:
                    return
                next_url = response.urljoin(self.page_selector.format(offset = self.page_offset))
            if next_url is not None:
                yield scrapy.Request(url=next_url, callback=self.parse, errback=self.handle_error)
