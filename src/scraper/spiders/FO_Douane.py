from scraper.spiders.BaseSpider import BaseSpider


class FO_Douane(BaseSpider):
    name = "FO_Douane"
    
    article_selector_in_list = ".lcp_catlist"
    article_link_selector_in_list = "li a ::attr(href)"
    article_title_selector_in_list = "li a ::text"
    article_date_selector_in_list = "li ::text"
    article_date_format_in_list = "%d %B %Y"
    article_html_selector = "div.entry-content p"
    article_file_selector = None

    page_index = 1
    page_selector = None

    start_urls = [
        'https://fodouanes.fr/sndfo/les-actualites-du-snd-fo/'
    ]
