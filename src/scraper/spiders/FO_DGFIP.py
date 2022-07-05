from scraper.spiders.BaseSpider import BaseSpider


class FO_DGFIP(BaseSpider):
    name = "FO_DGFIP"
    
    article_selector_in_list = ".card.shadow-lg"
    article_link_selector_in_list = ".card-text a ::attr(data-href)"
    article_title_selector_in_list = ".card-title b ::text"
    article_date_selector_in_list = ".badge.badge-warning ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "body"
    article_file_selector = "a ::attr(href)"

    page_index = 1
    page_selector = '?page={page}'

    start_urls = [
        'https://www.fo-dgfip.fr/'
    ]
