from scraper.spiders.BaseSpider import BaseSpider

class CFE_DGFIP(BaseSpider):
    name = "CFE_DGFIP"
    
    article_selector_in_list = "article"
    article_link_selector_in_list = "h2.title a::attr(href)"
    article_title_selector_in_list = "h2.title a::text"
    article_date_selector_in_list = ".post-info .thetime::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "article"
    article_file_selector = '.wp-block-file a::attr(href)'

    page_index = 1
    page_selector = 'page/{page}'

    start_urls = [
        'http://www.cgc-dgfip.info/category/actualites'
    ]

