from scraper.spiders.BaseSpider import BaseSpider


class FSU_FonctionPublique(BaseSpider):
    name = "FSU_FonctionPublique"
    
    article_selector_in_list = "blocarticle"
    article_link_selector_in_list = ".article-title a ::attr(href)"
    article_title_selector_in_list = ".article-title h2 ::text"
    article_date_selector_in_list = ".article-date ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "article"
    article_file_selector = "a ::attr(href)"

    page_index = 1
    page_selector = '?page={page}'

    start_urls = [
        'https://fsu.fr/category/nos-actions/communiques'
    ]
