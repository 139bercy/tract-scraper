from scraper.spiders.BaseSpider import BaseSpider


class UNSA_DGFIP(BaseSpider):
    name = "CGT_UFSE"

    article_selector_in_list = "#content ul li"
    article_link_selector_in_list = ".entry-title a ::attr(href)"
    article_title_selector_in_list = ".entry-title ::text"
    article_date_selector_in_list = ".info-publi ::text"
    article_date_format_in_list = "%d %m %Y"
    article_date_term_in_list = {
        "1er": "1",
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
        "décembre": "12",
        "lundi": "",
        "mardi": "",
        "mercredi": "",
        "jeudi": "",
        "vendredi": "",
        "samedi": "",
        "dimanche": "",
    }

    article_html_selector = ".text p ::text"
    article_file_selector = ".text p a ::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = ".lien_pagination"

    start_urls = [
        'https://ufsecgt.fr/spip.php?rubrique756'
    ]
