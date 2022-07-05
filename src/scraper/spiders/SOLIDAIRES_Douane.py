from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRE_Douane(BaseSpider):
    name = "SOLIDAIRE_Douane"
    
    article_selector_in_list = "#zone .lien_article"
    article_link_selector_in_list = " ::attr(href)"
    article_title_selector_in_list = ".titre ::text"
    article_date_selector_in_list = ".date ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "#zone"
    article_file_selector = "a ::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'http://www.solidaires-douanes.org'
    ]
