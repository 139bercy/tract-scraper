from scraper.spiders.BaseSpider import BaseSpider


class FO_Directe(BaseSpider):
    name = "FO_Directe"
    
    article_selector_in_list = "article.article"
    article_link_selector_in_list = ".entry-title a::attr(href)"
    article_title_selector_in_list = ".entry-title a::text"
    article_date_selector_in_list = ".publication time::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "article.article"
    article_file_selector = "a::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = '?debut_articles={offset}}#pagination_articles'

    start_urls = [
        'https://www.force-ouvriere.fr/+-DIRECTTE-+'
    ]
