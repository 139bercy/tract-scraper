from scrapy.utils.project import get_project_settings
from slugify import slugify
from scraper.utils.urlUtils import path_leaf
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import os
import shutil

settings = get_project_settings()


def writeFile(filename, content):
    if content is None:
        return
    directory = settings.get('FILES_STORE')
    filepath = os.path.join(directory, filename)
    if not in_downloads(filename):
        folder_path = os.path.dirname(filepath)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(filepath, encoding="utf-8", mode='w+') as file:
            file.write(content)
            file.close()


def to_html_filename(site, date, title):
    date_str = slugify(date.strftime("%d-%m-%y"))
    title_str = slugify(title)

    return f'{date_str}/{site}__{title_str}.html'


def to_filename(site, date, title, file):
    date_str = slugify(date.strftime("%d-%m-%y"))
    title_str = slugify(title)
    file_str = path_leaf(file)

    filename = f'{site}__{title_str}__{file_str}'
    if len(filename) > 250:
        filename = filename[: len(filename) - 270]
    return f'{date_str}/{filename}'


def in_downloads(filename): 
    directory = settings.get('FILES_STORE')
    filepath = os.path.join(directory, filename)

    return os.path.exists(filepath)


def purge_archives():
    directory_path = os.path.abspath(settings.get('FILES_ARCHIVE'))
    directory_folders = os.listdir(directory_path)
    for folder in directory_folders:
        folder_date = datetime.strptime(folder, "%d-%m-%y").date()
        min_date = date.today() - relativedelta(weeks=settings.get('WEEKS_TO_ARCHIVE'))
        if folder_date < min_date:
            folder_path = os.path.join(directory_path, folder)
            folder_files = os.listdir(folder_path)
            for file in folder_files:
                os.remove(os.path.join(folder_path, file))
            os.removedirs(folder_path)


def move_from_archives_to_downloads():
    archive_directory_path = os.path.abspath(settings.get('FILES_ARCHIVE'))
    archive_directory_folders = os.listdir(archive_directory_path)
    store_directory_path = os.path.abspath(settings.get('FILES_STORE'))
    for folder in archive_directory_folders:
        folder_date = datetime.strptime(folder, "%d-%m-%y").date()
        min_date = date.today() - relativedelta(weeks=settings.get('WEEKS_TO_SCRAP'))
        if folder_date > min_date:
            archive_folder_path = os.path.join(archive_directory_path, folder)
            archive_folder_files = os.listdir(archive_folder_path)
            store_folder_path = os.path.join(store_directory_path, folder)
            if not os.path.exists(store_folder_path):
                os.makedirs(store_folder_path)
            for file in archive_folder_files:
                file_source_path = os.path.join(archive_folder_path, file);
                file_target_path = os.path.join(store_folder_path, file);
                shutil.move(file_source_path, file_target_path)
            os.removedirs(os.path.join(archive_directory_path, folder))
