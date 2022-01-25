import os
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
from scraper.utils.fileUtils import writeFile

settings = get_project_settings()

class DownloadFilePipeline(FilesPipeline):

    extensions = settings.get('EXT_TO_SCRAP')

    def get_media_requests(self, item, info):
        file_type = item['type']
        if file_type == 'html':
            file_name = item['file_name']
            file_content = item['file_content']
            writeFile(f'{file_name}', file_content)
        else:
            file_url = item['file_url']
            if any(extension in file_url for extension in self.extensions):
                yield scrapy.Request(file_url)
            
    def file_path(self, request, response=None, info=None, *, item=None):
        extension = os.path.splitext(request.url)[1]
        name = item["file_name"]
        if extension in name:
            return name
        else:
            return f"{name}{extension}"