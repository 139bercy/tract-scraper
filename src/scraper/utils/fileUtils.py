from scrapy.utils.project import get_project_settings
from slugify import slugify
from scraper.utils.urlUtils import path_leaf
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import os
import re

settings = get_project_settings()

def writeFile(filename, content):
    if content is None:
        return
    directory = settings.get('FILES_STORE')
    filepath = os.path.join(directory, filename)
    if not in_archives(filename):
        with open(filepath, encoding="utf-8", mode='a+') as file:
            file.write(content)
            file.close()

def to_html_filename(site, date, title):
    date_str = slugify(date.strftime("%d%m%y"))
    title_str = slugify(title)

    return f'{site}__{date_str}__{title_str}.html'

def to_filename(site, date, title, file):
    date_str = slugify(date.strftime("%d%m%y"))
    title_str = slugify(title)
    file_str = path_leaf(file)

    return f'{site}__{date_str}__{title_str}__{file_str}'

def in_archives(filename): 
    directory = settings.get('FILES_ARCHIVE')
    filepath = os.path.join(directory, filename)

    return os.path.exists(filepath)

def purge_archives():
    directory = settings.get('FILES_ARCHIVE')
    directory_path = os.path.abspath(directory)
    directory_files = os.listdir(directory_path)
    for file in directory_files:
        match = re.search(r".*__(\d{6})__.*", path_leaf(file))
        file_date = datetime.strptime(match.groups()[0], "%d%m%y").date()
        min_date = date.today() - relativedelta(months=settings.get('MONTHS_TO_ARCHIVE'))
        if file_date < min_date:
            os.remove(os.path.join(directory_path, file))
