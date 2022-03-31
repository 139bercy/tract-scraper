from scraper.spiders.BaseSpider import BaseSpider

class CGT_Douane(BaseSpider):
    name = "CGT_Douane"
    
    article_selector_in_list = ".row.blog"
    article_link_selector_in_list = "h2 a::attr(href)"
    article_title_selector_in_list = "h2 a::text"
    article_date_selector_in_list = ".blog-info li::text"
    article_date_format_in_list = "%d %B %Y"
    article_date_term_in_list = {
        "1er": "1"
    }
    article_html_selector = ".news-v3"
    article_file_selector = 'dl a::attr(href)'

    page_offset = 0
    page_limit = 10
    page_selector = '?debut_derniersArticles={offset}#pagination_derniersArticles'

    start_urls = [
        'https://www.cgtdouanes.fr/'
    ]

