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
import pandas as pd


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
    article_date_unwanted_words = None
    article_count = 0

    article_html_selector = None
    article_file_selector = None

    page_index = None
    page_offset = None
    page_offset_step = None
    page_selector = None

    start_urls = []

    def parse_article_date(self, container):
        """
        Parse the article date from the container
        try to extract the date base on the
            article_date_selector_in_list,
            article_date_format_in_list,
            article_date_separator_in_list,
            article_date_term_in_list
        """
        datee = None
        if isinstance(self.article_date_selector_in_list, list):
            date_parts = []
            for date_selector in self.article_date_selector_in_list:
                date_part = container.css(date_selector).get().strip()
                if date_part is not None and self.article_date_term_in_list is not None:
                    for term in self.article_date_term_in_list:
                        date_part = date_part.replace(term, self.article_date_term_in_list[term]) 
                date_parts.append(date_part)
            datee = ' '.join(date_parts)
        else:
            datee = container.css(self.article_date_selector_in_list).get()
            if datee is not None and self.article_date_term_in_list is not None:
                for term in self.article_date_term_in_list:
                    datee = datee.replace(term, self.article_date_term_in_list[term])
        if datee is None or datee.isspace():
            return None

        date_str = str(datee.encode('utf-8').decode('utf-8')).strip()
        if self.article_date_separator_in_list is not None:
            date_str = date_str.split(self.article_date_separator_in_list)[-1].strip()
        if self.article_date_unwanted_words is not None:
            for word in self.article_date_unwanted_words:
                date_str = date_str.replace(word, "")
        return pd.to_datetime(date_str, format=self.article_date_format_in_list)

    def parse_article_url_in_list(self, response, container):
        url = container.css(self.article_link_selector_in_list).get()
        self.logger.info(f"Parsing article url {response.urljoin(str(url)).strip()}")
        return response.urljoin(str(url)).strip()

    def handle_error(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error(f'HttpError on {response.url}')

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error(f'DNSLookupError on {request.url}')

        elif failure.check(TimeoutError):
            request = failure.request
            self.logger.error(f'TimeoutError on {request.url}')

    def parse_article(self, response):
        """
        Parse the article page,
        Check if the article is already downloaded,
        If not, get the article information, file_name and file_content
        """
        article = response.css(self.article_html_selector)
        article_title = response.meta['article_title']
        article_date = response.meta['article_date']
        
        file_name = to_html_filename(self.name, article_date, article_title)
        file_content = article.get()

        # Check if the file already exists to avoid scrapping it again
        if not in_downloads(file_name):
            yield {
                    'type': 'html',
                    'file_name': file_name,
                    'file_content': file_content
                }

        # check if there is a file selector for the article
        if self.article_file_selector is None:
            return None

        # Get all files from the article
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
        self.logger.info(f"Starting to parse {response.url}")
        containers = response.css(self.article_selector_in_list)
        logger.info(f'{len(containers)} articles found in {response.url}')
        missing_date = 0
        article_date = pd.to_datetime("today")  # date.today()
        min_date = pd.to_datetime(article_date) - relativedelta(weeks=settings.get('WEEKS_TO_SCRAP'))
        if not containers:
            self.logger.warning(f"No articles found on the page {self.name}, wrong html selector ?")
        for container in containers:
            article_date = self.parse_article_date(container)
            if article_date is None or article_date < min_date:
                self.logger.debug(f"Article date is {article_date}, min date to compare to is {min_date}, article : "
                                  f"{container.css(self.article_title_selector_in_list).get()}")
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
                    logger.info(f'No file selector for {response.url}')
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
                yield scrapy.Request(url=article_url, callback=self.parse_article, errback=self.handle_error,
                                     meta=article_meta)

        if missing_date > 0:
            logger.info(f'{missing_date} articles not scrapped because the date missing')

        if article_date is not None and article_date > min_date:
            next_url = None
            if self.page_index is not None:
                self.page_index += 1
                if self.page_index >= 10:
                    return
                next_url = urljoin(clean_url(response.url), self.page_selector.format(page=self.page_index))
            elif self.page_offset is not None:
                self.page_offset += self.page_limit
                if self.page_offset >= 100:
                    return
                next_url = response.urljoin(self.page_selector.format(offset=self.page_offset))
            if next_url is not None:
                yield scrapy.Request(url=next_url, callback=self.parse, errback=self.handle_error)
