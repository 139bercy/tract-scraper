import os

BOT_NAME = 'scraper'
SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
LOG_LEVEL = 'INFO'

EXT_TO_SCRAP = [".pdf", ".doc", ".docx"]
WEEKS_TO_SCRAP = 1
WEEKS_TO_ARCHIVE = 3
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

FILES_STORE = None
FILES_ARCHIVE = None
if "DOCKERIZED" in os.environ:
    FILES_STORE = '/home/bercy/track-scraper/downloads'
    FILES_ARCHIVE = '/home/bercy/track-scraper/archives'
else:
    FILES_STORE = PROJECT_ROOT + '/downloads'
    FILES_ARCHIVE = PROJECT_ROOT + '/archives'    

RETRY_TIMES = 2
ITEM_PIPELINES = {
    'scraper.pipelines.DownloadFilePipeline': 1
}
ROBOTSTXT_OBEY = False
