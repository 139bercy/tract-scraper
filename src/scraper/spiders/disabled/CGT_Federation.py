from scraper.spiders.BaseSpider import BaseSpider

class CGT_Federation(BaseSpider):
    name = "CGT_Federation"
    
    article_selector_in_list = "li.u-block-hover"
    article_link_selector_in_list = "a.u-link-v2::attr(href)"
    article_title_selector_in_list = "h3::text"
    article_date_selector_in_list = [
        ".row .col-lg-2 span::text",
        ".row .col-lg-2 span.d-block::text"
    ]
    article_date_format_in_list = "%d %b %Y"
    article_date_term_in_list = {
        "jan": "janv.",
        "fév": "févr.",
        "mar": "mars",
        "avr": "avr.",
        "mai": "mai",
        "jui": "juil.",
        "aoû": "août",
        "sep": "sept.",
        "oct": "oct.",
        "nov": "nov.",
        "déc": "déc."
    }
    article_html_selector = "article"
    article_file_selector = 'a::attr(href)'

    page_offset = 0
    page_limit = 10
    page_selector = '?debut_articles={offset}'

    start_urls = [
        'https://www.cgtfinances.fr/actu'
    ]

