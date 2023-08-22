from selenium.webdriver.support import expected_conditions as EC

from pages.explore_page import ExplorePage
from util.util_links_checker import LinkChecker
from util.util_scraper import UrlScraper


class ExploreNeuronMorphologyPage(ExplorePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = ExplorePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_neuron_morphology_page(self):
        self.browser.get(self.url + "/explore/morphology")
        return self.browser.current_url
