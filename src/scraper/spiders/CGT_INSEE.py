from scraper.spiders.BaseSpider import BaseSpider


class CGT_INSEE(BaseSpider):
    name = "CGT_INSEE"
    
    article_selector_in_list = ".actu article"
    article_link_selector_in_list = "h3 a ::attr(href)"
    article_title_selector_in_list = "h3 a ::text"
    article_date_selector_in_list = [
        ".date .day ::text",
        ".date .month ::text",
        ".date .year ::text"
    ]
    article_date_term_in_list = {
        "janv": "janv.",
        "févr": "févr.",
        "mars": "mars",
        "avri": "avr.",
        "mai": "mai",
        "juin": "juin",
        "juil": "juil.",
        "août": "août",
        "sept": "sept.",
        "octo": "oct.",
        "nove": "nov.",
        "déce": "déc.",
        "1er": "1"
    }
    article_date_format_in_list = "%d %b %Y"

    article_html_selector = "article.article-complet"
    article_file_selector = "a ::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = '?debut_actualite={offset}#pagination_actualite'

    start_urls = [
        'https://www.cgtinsee.org/'
    ]
