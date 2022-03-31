from scraper.spiders.BaseSpider import BaseSpider

class CFE_Centrale(BaseSpider):
    name = "CFE_Centrale"
    
    article_selector_in_list = ".post"
    article_link_selector_in_list = ".post h1 a::attr(href)"
    article_title_selector_in_list = ".post h1 a:text"
    article_date_selector_in_list = ".post h4::text"
    article_date_format_in_list = "%B %d, %Y"
    article_html_selector = ".post"
    article_file_selector = None

    page_index = 1
    page_selector = "/page/{page}"

    start_urls = [
        'http://www.cgc-centrale.info'
    ]

