from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRE_CCRF_SCL(BaseSpider):
    name = "SOLIDAIRE_CCRF_SCL"

    article_selector_in_list = "#content .items-row"
    article_link_selector_in_list = ".tck-article-title a ::attr(href)"
    article_title_selector_in_list = ".tck-article-title a ::text"
    article_date_selector_in_list = "time ::text"
    article_date_format_in_list = "%d %m %Y"
    article_html_selector = ".tck-article-body"
    article_file_selector = '.noicon ::attr(href)'
    article_date_term_in_list = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "aout": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12",
    }

    page_index = 1
    page_selector = '/page/{page}'

    start_urls = [
        'http://www.solidaires-ccrf-scl.org/index.php/actualites/ccrf-et-scl'
    ]
