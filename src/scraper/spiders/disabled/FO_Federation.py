from scraper.spiders.BaseSpider import BaseSpider

class FO_Federation(BaseSpider):
    name = "FO_Federation"
    
    article_selector_in_list = "article"
    article_link_selector_in_list = ".entry-title a::attr(href)"
    article_title_selector_in_list = ".entry-title a::text"
    article_date_selector_in_list = ".date time::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "#main"
    article_file_selector = "a::attr(href)"

    page_index = 1
    page_selector = 'page/{page}/'

    start_urls = [
        'https://financesfo.fr/toutes-les-actualites'
    ]

