from scraper.spiders.BaseSpider import BaseSpider

class CFE_Conf(BaseSpider):
    name = "CFE_Conf"
    
    article_selector_in_list = ".slider_actu_style .bloc"
    article_link_selector_in_list = ".content a::attr(href)"
    article_title_selector_in_list = ".content a::text"
    article_date_selector_in_list = ".publi::text"
    article_date_format_in_list = "%d - %M - %Y"
    article_html_selector = "#main .container .col-lg-9"
    article_file_selector = None

    page_index = None
    page_selector = None

    start_urls = [
        'https://www.cfecgc.org/actualites'
    ]

