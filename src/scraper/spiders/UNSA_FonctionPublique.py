from scraper.spiders.BaseSpider import BaseSpider


class UNSA_FonctionPublique(BaseSpider):
    name = "UNSA_FonctionPublique"
    
    article_selector_in_list = ".post-item"
    article_link_selector_in_list = ".content-text h2 a::attr(href)"
    article_title_selector_in_list = ".content-text h2 a::text"
    article_date_selector_in_list = ".content-date::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = ".page-article-content"
    article_file_selector = "a::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'https://www.unsa-fp.org'
    ]
