from scraper.spiders.BaseSpider import BaseSpider


class FGF_FO_Fonctionnaire(BaseSpider):
    name = "FO_FGF_Fonctionnaire"

    article_selector_in_list = "#ulIdea li"
    article_link_selector_in_list = ".objectList_title a ::attr(href)"
    article_title_selector_in_list = ".objectList_title a ::text"
    article_date_selector_in_list = None
    article_date_format_in_list = None
    article_html_selector = "#main"
    article_file_selector = "a ::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'http://www.fo-fonctionnaires.fr/idea/?c='
    ]
