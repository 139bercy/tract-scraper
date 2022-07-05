from scraper.spiders.BaseSpider import BaseSpider


class UNSA_INSEE(BaseSpider):
    name = "UNSA_INSEE"
    
    article_selector_in_list = ".post"
    article_link_selector_in_list = ".entry-title a ::attr(href)"
    article_title_selector_in_list = ".entry-title a ::text"
    article_date_selector_in_list = ".entry-date ::text"
    article_date_format_in_list = "%B %d, %Y"
    article_html_selector = ".post"
    article_file_selector = "a ::attr(href)"

    page_index = 1
    page_selector = '?paged={page}'

    start_urls = [
        'https://uga-insee.fr'
    ]
