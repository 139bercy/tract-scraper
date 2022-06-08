from scraper.spiders.BaseSpider import BaseSpider


class FO_Douane(BaseSpider):
    name = "FO_Douane"
    
    article_selector_in_list = "table table"
    article_link_selector_in_list = None
    article_title_selector_in_list = "strong::text"
    article_date_selector_in_list = "font::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "table table"
    article_file_selector = "a::attr(href)"

    page_index = 1
    page_selector = None

    start_urls = [
        'http://fodouanes.fr/actualites.html'
    ]
