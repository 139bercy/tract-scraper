from scraper.spiders.BaseSpider import BaseSpider


class CGT_Centrale(BaseSpider):
    name = "CGT_Centrale"
    
    article_selector_in_list = ".row.blog"
    article_link_selector_in_list = "h2 a ::attr(href)"
    article_title_selector_in_list = "h2 a ::text"
    article_date_selector_in_list = ".blog-info li ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = ".news-v3"
    article_file_selector = 'p a ::attr(href)'

    page_offset = 0
    page_limit = 10
    page_selector = 'spip.php?page=actualite&debut_derniersArticles={offset}'

    start_urls = [
        'https://www.centralefinancescgt.fr/spip.php?page=actualite'
    ]
