from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRE_IDD(BaseSpider):
    name = "SOLIDAIRE_IDD"
    
    article_selector_in_list = ".items-row"
    article_link_selector_in_list = None
    article_title_selector_in_list = ".item-title ::text"
    article_date_selector_in_list = ".create time ::text"
    article_date_format_in_list = "Création : %d %B %Y"
    article_html_selector = ".items-row"
    article_file_selector = "a ::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = "?start={offset}"

    start_urls = [
        'http://solidairesidd.com/'
    ]
