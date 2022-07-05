from scraper.spiders.BaseSpider import BaseSpider


class CGT_Finances(BaseSpider):
    name = "CGT_Finances"
    
    article_selector_in_list = ".views-row.article"
    article_link_selector_in_list = "h2 a ::attr(href)"
    article_title_selector_in_list = "h2 a ::text"
    article_date_selector_in_list = ".article-date ::text"
    article_date_format_in_list = "%A, %d %B, %Y - %H:%M"
    article_html_selector = "article"
    article_file_selector = '.file a ::attr(href)'

    page_index = 1
    page_selector = '/accueil?page={page}'

    start_urls = [
        'http://www.financespubliques.cgt.fr'
    ]
