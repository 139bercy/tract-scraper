from scraper.spiders.BaseSpider import BaseSpider

class FSU_Federation(BaseSpider):
    name = "FSU_Federation"
    
    article_selector_in_list = ".hotwp-fp04-post"
    article_link_selector_in_list = ".hotwp-fp04-post-title a::attr(href)"
    article_title_selector_in_list = ".hotwp-fp04-post-title a::text"
    article_date_selector_in_list = ".hotwp-fp04-post-date::text"
    article_date_format_in_list = "%d/%m/%Y"
    article_html_selector = "article"
    article_file_selector = "a::attr(href)"

    page_index = 1
    page_selector = 'page/{page}'

    start_urls = [
        'https://www.fsu-finances.fr/category/directions/'
    ]

