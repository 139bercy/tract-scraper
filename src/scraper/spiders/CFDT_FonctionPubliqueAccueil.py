from scraper.spiders.BaseSpider import BaseSpider


class CFDT_FonctionPubliqueAccueil(BaseSpider):
    name = "CFDT_FonctionPubliqueAccueil"
    
    article_selector_in_list = ".article-left"
    article_link_selector_in_list = "a::attr(href)"
    article_title_selector_in_list = "h3::text"
    article_date_selector_in_list = "div.date > span::text"
    article_date_format_in_list = "%d/%m/%Y"
    article_html_selector = "article"
    article_file_selector = "a::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = "?PortalAction_rwd_368730_start={offset}&PortalAction_rwd_368730_pageSize=10"

    start_urls = [
        "https://uffa.cfdt.fr/portail/uffa/d-d-i-recette_12432"
    ]
