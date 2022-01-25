from scraper.spiders.BaseSpider import BaseSpider

class CFTC_Finance(BaseSpider):
    name = "CFTC_Finance"
    
    article_selector_in_list = "article"
    article_link_selector_in_list = ".entry-title a::attr(href)"
    article_title_selector_in_list = ".entry-title a::text"
    article_date_selector_in_list = ".entry-footer time::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "article"
    article_file_selector = '.entry-content a::attr(href)'

    page_index = 1
    page_selector = '/page/{page}'

    start_urls = [
        'http://www.cftc-finances.org/category/publications'
    ]

