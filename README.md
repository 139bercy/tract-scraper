[![CircleCI](https://dl.circleci.com/status-badge/img/gh/139bercy/tract-scraper/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/139bercy/tract-scraper/tree/main)
# Installation and execution

After cloning the project, *cd* in the project directory and execute the following command lines.

## In a local environment

Create a virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
. venv/scripts/activate
```

Install the program requirements:

```
pip install -r requirements.txt
```

Export the environment variable *SCRAPY_SETTINGS_MODULE*:

```
export SCRAPY_SETTINGS_MODULE='scraper.settings'
```

Create two folders respecting the following treeview:

```
src/scraper/downloads
src/scraper/archives
```
Execute the application:

```
python3 src/main.py
```

Or scrappe only one site:

```
python3 src/main.py -S UNSA_DGFIP
```
```
python3 src/main.py --Spider UNSA_DGFIP
```
## In a Docker environment

You can also deployed the application using ***Docker*** by simply running the code line:
```
docker-compose up
```

# Settings

The application can be configured via some variables available in the *settings.py* file located in the directory :

```
src/scraper/
```

The application can scrap articles and files from weeks back. This number of weeks can be configured using the *WEEKS_TO_SCRAP* variable.
```
WEEKS_TO_SCRAP = 2
```

The downloaded content can be archived during a certain period of time (expressed in weeks) which can be set in the WEEKS_TO_ARCHIVE variable.

```
WEEKS_TO_ARCHIVE = 3
```

In addition to scraping some HTML content, the application can also download some files which extensions can be filtered in the *EXT_TO_SCRAP* variable.

```
EXT_TO_SCRAP = [".pdf", ".doc", ".docx"]
```





# Results
Depending on the number of websites to scrap, the process should not even take a minute.

At the end of the process, all the downloaded files will be find in the ***downloads*** folder.

When the application is deployed, the CI pipeline is in charge to automatically move the files from the ***downloads*** folder to the ***archives*** folder before each run.

In a local environment, these files have to be moved manually in the ***archives*** folder.


# Add site to the list
Copy the template file `src/scrapper/spiders/template.py` and rename it to `<website_name>.py`.

Add ` ::text` to the end of Html DOM element to get the text content, or ` ::attr("href")` to get the href attribute.

- `article_selector_in_list` `str` Html DOM selector to locate all articles on the website.
- `article_link_selector_in_list` `str` Html DOM selector to locate the link of each article. be aware that the DOM is now a child of `article_selector_in_list` so you don't have to rewrite all the DOM dependencies.
- `article_title_selector_in_list` `str` Html DOM selector to locate the title of each article. be aware that the DOM is now a child of `article_selector_in_list` so you don't have to rewrite all the DOM dependencies.
- `article_date_selector_in_list` `str` Html DOM selector to locate the date of each article. be aware that the DOM is now a child of `article_selector_in_list` so you don't have to rewrite all the DOM dependencies.
- `article_date_format_in_list` `str` Date format of the date to scrap. Such as `%d/%m/%Y` or `%Y-%m-%d`.
- `article_date_term_in_list` `str` Dictionary of terms to replace in the date. Such as `{'1er': '1', 'janvier': '01', 'fevr': '02'}`.
- `article_date_separator_in_list` `str` separator to remove unwanted string in the date example : `Communiqué : 28 juin 2022` -> `28 juin 2022`
 
Page navigation :
- `page_offset` `INT` Increment the page number to scrap.
- `page_limit` `INT` Max number of page to click.
- `page_index` `INT` Index of the starting page.
- `page_selector` `str` String to add to the url to get to the next page. May require `page_index`, `page_limit` and `page_offset`.

You are in the article now for the following selectors (don't forget to click the article to find the new DOM):
- `article_html_selector` `str` Html DOM selector to locate the html content of the article.
- `article_file_selector` `str` Html DOM selector to locate the file of the article that will be downloaded.