from scraper.spiders.BaseSpider import BaseSpider


class CFTC_Centrale(BaseSpider):
    name = "CFTC_Centrale"
    
    article_selector_in_list = "article"
    article_link_selector_in_list = ".entry-header .entry-title a ::attr(href)"
    article_title_selector_in_list = ".entry-header .entry-title a ::text"
    article_date_selector_in_list = ".entry-meta .date-i a ::text"
    article_date_format_in_list = "%d %B %Y at %H h %M min"
    article_html_selector = "article"
    article_file_selector = '.entry-content p a ::attr(href)'

    page_index = 1
    page_selector = 'page/{page}'

    start_urls = [
        'http://cftc-centrale-finances.fr'
    ]
