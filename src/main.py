from scrapy import spiderloader    
from scrapy.utils.project import get_project_settings
from scraper.utils.fileUtils import purge_archives, move_from_archives_to_downloads

from scrapy.crawler import CrawlerProcess
import locale
import logging

logger = logging.getLogger()
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

def main():
    purge_archives()
    move_from_archives_to_downloads()
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)
    spiders = spider_loader.list()
    logger.info(f'{len(spiders)} spiders found.')
    for spider_name in spider_loader.list():
        logger.info(f'Registers {spider_name} spider.')
        process.crawl(spider_name)
    process.start()
    logger.info(f"Scrapping DONE!")

if __name__ == "__main__":
    main()