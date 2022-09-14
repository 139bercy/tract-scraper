from scraper.spiders.BaseSpider import BaseSpider


class TEMPLATE(BaseSpider):
    name = "TEMPLATE"

    article_selector_in_list = None
    article_link_selector_in_list = None
    article_title_selector_in_list = None
    article_date_selector_in_list = None
    article_date_format_in_list = None
    """
    Code 	Meaning 	            Example
    %d 	    Two-digit day 	        01-31
    %a 	    Weekday abbreviation 	Sun
    %A 	    Weekday 	            Sunday
    %m 	    Two-digit month 	    01-12
    %b 	    Month abbreviation 	    Jan
    %B 	    Month 	                January
    %y 	    Two-digit year 	        09
    %Y 	    Four-digit year 	    2009
    
    https://docs.python.org/fr/3/library/datetime.html#strftime-and-strptime-format-codes
    """
    article_date_term_in_list = None
    article_date_separator_in_list = None

    article_html_selector = None
    article_file_selector = None

    page_offset = None
    page_limit = None
    page_index = None
    page_selector = None

    start_urls = [
        'http://template.scraper'
    ]
