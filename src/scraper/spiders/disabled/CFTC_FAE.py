from scraper.spiders.BaseSpider import BaseSpider

class CFTC_FAE(BaseSpider):
    name = "CFTC_FAE"
    
    article_selector_in_list = ".card"
    article_link_selector_in_list = ".card-body a::attr(href)"
    article_title_selector_in_list = ".card-body a h3::text"
    article_date_selector_in_list = ".card-text.text-muted::text"
    article_date_format_in_list = "%d %b %Y"
    article_date_separator_in_list = ':'
    article_html_selector = ".editorial"
    article_file_selector = 'a.float-end.btn.btn-info::attr(href)'

    page_index = 1
    page_selector = '?page={page}'

    start_urls = [
        'http://www.cftc-fae.fr'
    ]

