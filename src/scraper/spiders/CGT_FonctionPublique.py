from scraper.spiders.BaseSpider import BaseSpider


class CGT_FonctionPublique(BaseSpider):
    name = "CGT_FonctionPublique"
    
    article_selector_in_list = ".item"
    article_link_selector_in_list = "h3 a::attr(href)"
    article_title_selector_in_list = "h3 a::text"
    article_date_selector_in_list = ".info-publi .published::text"
    article_date_format_in_list = "%A %d %B %Y"
    article_date_term_in_list = {
        "1er": "1"
    }
    article_html_selector = ".contenu-principal"
    article_file_selector = 'a::attr(href)'

    page_offset = 0
    page_limit = 10
    page_selector = '/spip.php?rubrique756&debut_derniers_articles={offset}#pagination_derniers_articles'

    start_urls = [
        'http://ufsecgt.fr/spip.php?rubrique756'
    ]
