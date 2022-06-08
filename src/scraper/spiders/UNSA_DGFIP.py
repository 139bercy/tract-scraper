from scraper.spiders.BaseSpider import BaseSpider


class UNSA_DGFIP(BaseSpider):
    name = "UNSA_DGFIP"
    
    article_selector_in_list = ".content-category .category tr"
    article_link_selector_in_list = ".list-title a::attr(href)"
    article_title_selector_in_list = ".list-title a::text"
    article_date_selector_in_list = ".list-date::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "#jsn-mainbody"
    article_file_selector = "a::attr(href)"

    page_offset = 0
    page_limit = 10
    page_selector = "?start={offset}"

    start_urls = [
        'http://www.unsadgfip.fr/actualite'
    ]
