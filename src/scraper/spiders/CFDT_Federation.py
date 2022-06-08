from scraper.spiders.BaseSpider import BaseSpider


class CFDT_Federation(BaseSpider):
    name = "CFDT_Federation"
    
    article_selector_in_list = ".article-left"
    article_link_selector_in_list = "a::attr(href)"
    article_title_selector_in_list = "h3::text"
    article_date_selector_in_list = ".date span::text"
    article_date_format_in_list = "%d/%m/%Y"
    article_html_selector = "article"
    article_file_selector = "a::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = "?PortalAction_rwd_368730_start={offset}&PortalAction_rwd_368730_pageSize=10"

    start_urls = [
        'https://finances.cfdt.fr/portail/finance/actualites-federales/ministeres-srv1_259208',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/finances-publiques/actualite-srv1_250764',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/douane/actualite-srv1_256796',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/centrales-ecoles/actualite-srv1_252339',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/dgccrf-laboratoires/actualite-srv1_256802',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/insee/actualite-srv1_256743',
        'https://finances.cfdt.fr/portail/finance/actualites-federales/a-la-une-recette_13295'
    ]
