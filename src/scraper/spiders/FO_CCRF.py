from datetime import datetime

from scraper.spiders.BaseSpider import BaseSpider


class FO_CCRF(BaseSpider):
    name = "FO_CCRF"

    article_selector_in_list = "#content_area"
    article_link_selector_in_list = ".j-downloadDocument a ::attr(href)"
    article_title_selector_in_list = ".j-downloadDocument .cc-m-download-title ::text"
    article_date_selector_in_list = ".j-downloadDocument .cc-m-download-title ::text"
    article_date_format_in_list = "%d %m %Y"
    article_date_term_in_list = {
        "janvier": "01",
        "février": "02",
        "mars": "03",
        "avril": "04",
        "mai": "05",
        "juin": "06",
        "juillet": "07",
        "août": "08",
        "septembre": "09",
        "octobre": "10",
        "novembre": "11",
        "décembre": "12"
    }
    article_date_separator_in_list = "just so in go in the parse_article_date fonction"

    article_html_selector = None
    article_file_selector = None

    start_urls = [
        'https://www.ccrf-force-ouvriere.fr/activit%C3%A9-syndicale-ccrf-bercy-et-ddi/actualit%C3%A9s-ccrf/'
    ]

    def parse_article_date(self, container):
        """
        Parse the article date from the container
        try to extract the date base on the
            article_date_selector_in_list,
            article_date_format_in_list,
            article_date_separator_in_list,
            article_date_term_in_list
        """
        date = None
        if isinstance(self.article_date_selector_in_list, list):
            date_parts = []
            for date_selector in self.article_date_selector_in_list:
                date_part = container.css(date_selector).get().strip()
                if date_part is not None and self.article_date_term_in_list is not None:
                    for term in self.article_date_term_in_list:
                        date_part = date_part.replace(term, self.article_date_term_in_list[term])
                date_parts.append(date_part)
            date = ' '.join(date_parts)
        else:
            date = container.css(self.article_date_selector_in_list).get()
            if date is not None and self.article_date_term_in_list is not None:
                for term in self.article_date_term_in_list:
                    date = date.replace(term, self.article_date_term_in_list[term])

        if date is None or date.isspace():
            return None

        date_str = str(date.encode('utf-8').decode('utf-8')).strip()
        if self.article_date_separator_in_list is not None:
            # need to separate the date from the title date is always between "du" and ":"
            date_str = date_str.partition("du ")[2].split(':')[0].rstrip()
        return datetime.strptime(date_str, self.article_date_format_in_list).date()
