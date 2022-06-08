from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRE_Federation(BaseSpider):
    name = "SOLIDAIRE_Federation"
    
    article_selector_in_list = ".item"
    article_link_selector_in_list = None
    article_title_selector_in_list = ".item-title::text"
    article_date_selector_in_list = ".published time::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "#zone"
    article_file_selector = "a::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'http://www.solidairesfinances.fr/'
    ]
