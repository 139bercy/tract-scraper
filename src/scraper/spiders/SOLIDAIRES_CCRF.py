from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRES_CCRF(BaseSpider):
    name = "SOLIDAIRES_CCRF"
    
    article_selector_in_list = ".items-row"
    article_link_selector_in_list = ".item-title a ::attr(href)"
    article_title_selector_in_list = ".item-title a ::text"
    article_date_selector_in_list = ".published time ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = ".tck-article.item-page"
    article_file_selector = "a ::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'http://www.solidaires-ccrf-scl.org/'
    ]
