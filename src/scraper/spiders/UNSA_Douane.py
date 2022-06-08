from scraper.spiders.BaseSpider import BaseSpider


class UNSA_Douane(BaseSpider):
    name = "UNSA_Douane"
    
    article_selector_in_list = ".item-list li"
    article_link_selector_in_list = ".field-content a::attr(href)"
    article_title_selector_in_list = ".field-content a::text"
    article_date_selector_in_list = ".field-content time::text"
    article_date_format_in_list = "%A %d %B %Y"
    article_html_selector = "#contenu"
    article_file_selector = "a::attr(href)"

    page_index = None
    page_selector = None

    start_urls = [
        'http://www.unsadouanes.fr/index.php/fr/publications'
    ]
