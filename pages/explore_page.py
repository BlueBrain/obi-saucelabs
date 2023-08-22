from locators.explore_page_locators import ExplorePageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from util.util_links_checker import LinkChecker
from util.util_scraper import UrlScraper


class ExplorePage(HomePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = HomePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_page(self):
        self.browser.get(self.url + "/explore")
        return self.browser.current_url

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def wait_for_dynamically_loaded_links(self):
        self.wait.until(EC.presence_of_element_located(ExplorePageLocators.EXPLORE_LINK1))

    def check_explore_title_is_present(self):
        return self.wait.until(EC.element_to_be_clickable(ExplorePageLocators.EXPLORE_TITLE))

    def experimental_data_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.EXPERIMENTAL_DATA))

    def brain_models_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.BRAIN_MODELS))

    def brain_models_links(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.BRAIN_MODELS_LINK))

    def simulations_link(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.SIMULATIONS_LINK))

    def simulations_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.SIMULATIONS))

    def brain_and_cell_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.BRAIN_CELL_ANNOTATIONS))

    def portals_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.PORTALS))

    def gallery_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.GALLERY))

    def literature_title(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.LITERATURE))

    def experimental_data_button(self, timeout=10):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.EXPERIMENTAL_DATA_BUTTON))

    def neuron_electrophysiology_link(self):
        return self.wait.until(EC.presence_of_element_located(ExplorePageLocators.NEURON_ELECTROPHYSIOLOGY))

    def neuron_morphology_link(self):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.NEURON_MORPHOLOGY))

    def bouton_density_link(self):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.BOUTON_DENSITY))

    def neuron_density_link(self):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.NEURON_DENSITY))

    def layer_thickness_link(self):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.LAYER_THICKNESS))

    def synapse_per_connection_link(self):
        return self.wait.until(EC.visibility_of_element_located(ExplorePageLocators.SYNAPSE_PER_CONNECTION))

