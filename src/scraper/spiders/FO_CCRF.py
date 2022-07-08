from scraper.spiders.BaseSpider import BaseSpider


class FO_CCRF(BaseSpider):
    name = "FO_CCRF"

    article_selector_in_list = "#content_area"
    article_link_selector_in_list = ".j-downloadDocument a ::attr(href)"
    article_title_selector_in_list = ".j-downloadDocument .cc-m-download-title ::text"
    article_date_selector_in_list = ".j-downloadDocument .cc-m-download-title ::text"
    article_date_format_in_list = "%d %m %Y"
    article_date_term_in_list = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12"
    }
    article_date_separator_in_list = {"du",
                                      ":"}

    article_html_selector = None
    article_file_selector = None

    start_urls = [
        'https://www.ccrf-force-ouvriere.fr/activit%C3%A9-syndicale-ccrf-bercy-et-ddi/actualit%C3%A9s-ccrf/'
    ]
