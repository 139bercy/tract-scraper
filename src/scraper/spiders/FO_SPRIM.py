from scraper.spiders.BaseSpider import BaseSpider


class FO_SPRIM(BaseSpider):
    name = "FO_SPRIM"
    
    article_selector_in_list = "article.post"
    article_link_selector_in_list = "a.more-link::attr(href)"
    article_title_selector_in_list = ".entry-content p::text"
    article_date_selector_in_list = ".entry-date::text"
    article_date_format_in_list = "%d %B %Y"
    article_date_term_in_list = {
        "1er" : "1"
    }
    article_html_selector = "#content article"
    article_file_selector = "a::attr(href)"

    page_index = 1
    page_selector = 'page/{page}'

    start_urls = [
        'https://sprim-fo.org/blog/'
    ]
