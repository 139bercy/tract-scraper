from scraper.spiders.BaseSpider import BaseSpider


class CGT_Federation(BaseSpider):
    name = "CGT_Federation"
    
    article_selector_in_list = "li.u-block-hover"
    article_link_selector_in_list = "a.u-link-v2 ::attr(href)"
    article_title_selector_in_list = "h3 ::text"
    article_date_selector_in_list = [
        ".row .col-lg-2 span ::text",
        ".row .col-lg-2 span.d-block ::text"
    ]
    article_date_format_in_list = "%d %m %Y"
    article_date_term_in_list = {
        "jan": "01",
        "fév": "02",
        "mar": "03",
        "avr": "04",
        "mai": "05",
        "jui": "06",
        "aoû": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "déc": "12"
    }  # manque juillet juin = jui juillet = ???? confus
    article_html_selector = "article"
    article_file_selector = 'a ::attr(href)'

    page_offset = 0
    page_limit = 10
    page_selector = '?debut_articles={offset}'

    start_urls = [
        'https://www.cgtfinances.fr/actu'
    ]
