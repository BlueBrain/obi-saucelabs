from util.util_scraper import UrlScraper


def write_links_to_file(file_path, links):
    url_scraper = UrlScraper()
    url_scraper.write_links_to_file(links, file_path, mode='a')