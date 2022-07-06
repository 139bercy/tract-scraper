from scraper.spiders.BaseSpider import BaseSpider


class TEMPLATE(BaseSpider):
    name = "TEMPLATE"

    article_selector_in_list = None
    article_link_selector_in_list = None
    article_title_selector_in_list = None
    article_date_selector_in_list = None
    article_date_format_in_list = None
    article_date_term_in_list = None
    article_date_separator_in_list = None

    article_html_selector = None
    article_file_selector = None

    page_offset = None
    page_limit = None
    page_index = None
    page_selector = None

    start_urls = [
        'http://template.scraper'
    ]
