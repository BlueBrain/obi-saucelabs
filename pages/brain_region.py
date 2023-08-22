from locators.build_page_locators import BuildPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import CustomBasePage
from seleniumbase import BaseCase
from pages.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from urllib.parse import urlparse, parse_qs
from util.util_scraper import UrlScraper


class BrainRegionPage(HomePage, CustomBasePage):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.login_page = HomePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_config_page(self):
        # return self.browser.get(
        #     "https://bbp.epfl.ch/mmb-beta/build/cell-composition/interactive?brainModelConfigId=8a962b3a-2005-4bc1-9b35-c20c2ec4cc54")
        # "https://bbp.epfl.ch/mmb-beta/build/cell-composition/interactive?brainModelConfigId=526807b3-57d2-463a-9af4-f15c4450c677"
        config_id = '526807b3-57d2-463a-9af4-f15c4450c677'  # Set the desired config ID
        config_url = f"https://bbp.epfl.ch/mmb-beta/build/cell-composition/interactive?brainModelConfigId={config_id}"
        self.browser.get(config_url)
        return config_url

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def find_build_main_section(self):
        return self.wait.until(EC.presence_of_element_located(BuildPageLocators.BRAIN_BUILD_SECTION_MAIN))

    def open_build_div(self):
        return self.wait.until(EC.presence_of_element_located(BuildPageLocators.BRAIN_BUILD_CLOSED_DIV))

    def find_visible_basic_cells(self):
        return self.wait.until(EC.visibility_of_element_located(BuildPageLocators.VISIBLE_BASIC_CELL_GROUPS_TEXT))

    def find_basic_cells_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.BASIC_CELL_GROUPS_ARROW_BTN))

    def find_brain_stem_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.BRAIN_STEM_BTN))

    def find_cerebrum_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CEREBRUM_ARROW_BTN))

    def find_cerebral_cortex_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CEREBRAL_CORTEX_BTN))

    def find_cortical_plate_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CORTICAL_PLATE_BTN))

    def find_isocortex_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.ISOCORTEX_BTN))

    def find_agranular_ins_area_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.AGRANULAR_INS_AREA_BTN))

    def find_agranular_ins_area_dorsal_p_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.AGRANULAR_INS_AREA_DORSAL_P_BTN))

    def find_agranular_ins_area_dorsal_p_title(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.AGRANULAR_INS_AREA_DORSAL_P_TITLE))

    def find_configuration_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.SUB_MENU_CONFIGURATION))

    def l5_bp_arrow_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.L5_BP_ARROW_BTN))

    def l5_bp_slider_handle(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.L5_BP_SLIDER_HANDLE))

    def find_second_sub_menu(self):
        return self.wait.until(EC.visibility_of_element_located(BuildPageLocators.SECOND_SUB_MENU))

    def configuration_button(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.SUB_MENU_CONFIGURATION))

    def find_top_nav_menu(self):
        return self.wait.until(EC.presence_of_element_located(BuildPageLocators.TOP_NAV_MENU))

    def find_cell_composition(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CELL_COMPOSITION))

    def find_cell_model_assignment(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CELL_MODEL_ASSIGNMENT))

    def find_connectome_definition(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CONNECTOME_DEFINITION))

    def find_connection_model_assignment(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.CONNECTION_MODEL_ASSIGNMENT))

    def find_build_and_simulate_button(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.BUILD_AND_SIMULATE_BUTTON))

    def find_interactive_btn(self):
        return self.wait.until(EC.element_to_be_clickable(BuildPageLocators.SUB_MENU_INTERACTIVE))