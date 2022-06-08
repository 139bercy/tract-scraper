from scraper.spiders.BaseSpider import BaseSpider


class CFTC_DGFIP(BaseSpider):
    name = "CFTC_DGFIP"
    
    article_selector_in_list = "article"
    article_link_selector_in_list = ".entry-header .entry-title a::attr(href)"
    article_title_selector_in_list = ".entry-header .entry-title a::text"
    article_date_selector_in_list = ".entry-footer .entry-date::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "article"
    article_file_selector = '.wp-block-file a::attr(href)'

    page_index = 1
    page_selector = 'page/{page}'

    start_urls = [
        'https://www.cftc-dgfip.fr'
    ]
