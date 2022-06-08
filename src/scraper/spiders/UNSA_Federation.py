from scraper.spiders.BaseSpider import BaseSpider


class UNSA_Federation(BaseSpider):
    name = "UNSA_Federation"
    
    article_selector_in_list = "article.post"
    article_link_selector_in_list = ".post-title a::attr(href)"
    article_title_selector_in_list = ".post-title a::text"
    article_date_selector_in_list = ".post-date time::text"
    article_date_format_in_list = "%A %d %B %Y"
    article_html_selector = "article.post"
    article_file_selector = "a::attr(href)"

    page_index = 0
    page_selector = 'page/{page}'

    start_urls = [
        'https://finances.unsa.org'
    ]
