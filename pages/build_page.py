from locators.build_page_locators import BuildPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from util.util_methods import click_element, find_element, assert_element_text, \
    find_visibility_of_all_elements, find_all_elements, find_element_visibility, wait_for_long_load
from urllib.parse import urlparse, parse_qs
from util.util_scraper import UrlScraper


class BuildPage(HomePage):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.login_page = HomePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_build_page(self):
        self.browser.get(self.url + "/build/load-brain-config")
        return self.browser.current_url

    # def go_to_build_page(self):
    #     self.browser.get("http://localhost:3000/build/load-brain-config")

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def find_recent_configurations(self):
        return find_element(self.wait, BuildPageLocators.RECENT_CONFIGURATIONS)

    def verify_release_version(self):
        return find_element(self.wait, BuildPageLocators.RELEASE_VERSION)

    def select_default_config(self):
        return find_element(self.wait, BuildPageLocators.BUILD_PAGE_CLICK_PLUS_ICON)

    def find_config_search_field(self):
        return find_element_visibility(self.wait, BuildPageLocators.CONFIG_SEARCH_FIELD)

    def use_custom_config(self):
        return click_element(self.wait, BuildPageLocators.CUSTOM_MODEL_CONFIG)

    def clone_custom_config(self):
        return find_element(self.wait, BuildPageLocators.BTN_CLONE_CONFIG)

    # def clone_custom_config(self):
    #     return self.wait.until(
    #         lambda d: EC.presence_of_element_located(BuildPageLocators.BTN_CLONE_CONFIG)(d)
    #     )

    def find_edit_config_modal(self):
        return find_element_visibility(self.wait, BuildPageLocators.EDIT_MODAL)

    def find_default_config_name(self):
        return find_element_visibility(self.wait, BuildPageLocators.CONFIG_TEXT_FIELD_NAME)

    def set_your_config_name(self):
        return find_element_visibility(self.wait, BuildPageLocators.CHANGE_CONFIG_NAME_TEXT_FIELD)

    def clear_default_description_name(self):
        return find_element_visibility(self.wait, BuildPageLocators.DESCRIPTION)

    def set_config_description(self):
        return find_element_visibility(self.wait, BuildPageLocators.DESCRIPTION)

    def click_on_description(self):
        return find_element_visibility(self.wait, BuildPageLocators.DESCRIPTION)

    def find_start_editing_btn(self):
        return find_element(self.wait, BuildPageLocators.BTN_START_EDITING)

    def is_start_ed_btn_clickable(self):
        try:
            self.wait.until(EC.element_to_be_clickable(BuildPageLocators.BTN_START_EDITING))
            return True  # Button is clickable, so it is not disabled
        except TimeoutException:
            return False  # Button is not clickable, so it is disabled

    def push_start_editing(self):
        click_element(self.wait, BuildPageLocators.BTN_START_EDITING)
        wait_for_long_load(self.wait, BuildPageLocators.BTN_START_EDITING)

    def is_config_page_loaded(self):
        current_url = self.browser.current_url
        expected_url = self.generate_expected_url(current_url)
        print("This is 'is_config_page_loaded URL", expected_url)
        try:
            self.wait.until(lambda d: self.browser.current_url == expected_url)
            return True
        except TimeoutException:
            return False

    def generate_expected_url(self, current_url):
        url_parts = urlparse(current_url)
        query_params = parse_qs(url_parts.query)
        config_id = query_params.get(b'brainModelConfig', [b''])[0].decode('utf-8')
        expected_url = f"https://bbp.epfl.ch/mmb-beta/build/cell-composition/interactive?brainModelConfigId={config_id}"
        return expected_url

    def find_basic_cell_groups(self):
        return find_element(self.wait, BuildPageLocators.BASIC_CELL_GROUPS_AND_REGIONS)
