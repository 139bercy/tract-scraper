from scraper.spiders.BaseSpider import BaseSpider


class SOLIDAIRE_FinancesPubliques(BaseSpider):
    name = "SOLIDAIRE_FinancesPubliques"
    
    article_selector_in_list = "item"
    article_link_selector_in_list = "link ::text"
    article_title_selector_in_list = "title ::text"
    article_date_selector_in_list = "pubDate ::text"
    article_date_format_in_list = "%d %b %Y %H:%M:%S "
    article_date_term_in_list = {
        "Jan": "janv",
        "Feb": "févr",
        "Mar": "mars",
        "Apr": "avr",
        "May": "mai",
        "Jun": "juin",
        "Jul": "juil",
        "Aug": "août",
        "Sep": "sept",
        "Oct": "oct",
        "Nov": "nov",
        "Dec": "déc",
        "Mon": "",
        "Tue": "",
        "Wed": "",
        "Thu": "",
        "Fri": "",
        "Sat": "",
        "Sun": ""
    }
    article_date_separator_in_list = ", "
    article_date_unwanted_words = ["CEST", "CET"]
    article_html_selector = ".item-page"
    article_file_selector = "a ::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'https://sections.solidairesfinancespubliques.info/rss/rss.xml'
    ]
