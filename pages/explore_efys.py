from locators.explore_ephys_locators import ExploreEphysPageLocators
from selenium.webdriver.support import expected_conditions as EC
from util.util_methods import click_element, find_element, assert_element_text, \
    find_visibility_of_all_elements, find_all_elements
from pages.explore_page import ExplorePage
from util.util_links_checker import LinkChecker
from util.util_scraper import UrlScraper


class ExploreElectrophysiologyPage(ExplorePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = ExplorePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_ephys_page(self):
        self.browser.get(self.url + "/explore/electrophysiology")
        return self.browser.current_url

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def find_ephys_page_title(self):
        return find_element(self.wait, ExploreEphysPageLocators.NEURON_EPHYS_PAGE_TITLE)

    def find_brain_region_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.BRAIN_REGION_COLUMN)

    def find_e_type_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.E_TYPE_COLUMN)

    def find_name_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.NAME_REGION_COLUMN)

    def find_species_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.SPECIES_REGION_COLUMN)

    def find_contributors_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.CONTRIBUTORS_COLUMN)

    def find_creation_date_header(self):
        return find_element(self.wait, ExploreEphysPageLocators.CREATION_DATE_COLUMN)

    def find_search_button(self):
        return find_element(self.wait, ExploreEphysPageLocators.SEARCH_BUTTON)

    def find_search_input_search_item(self):
        return find_element(self.wait, ExploreEphysPageLocators.SEARCH_INPUT_FIELD)

    def find_filter_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.FILTER_BTN)

    def find_filter_close_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.FILTER_CLOSE_BTN)

    def find_plus_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.SIDE_BAR_PLUS_BTN)

    def find_side_bar_explore_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.SIDE_BAR_EXPLORE_BTN)

    def find_side_bar_plus_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.SIDE_BAR_PLUS_BTN)

    def find_side_bar_menu(self):
        return find_element(self.wait, ExploreEphysPageLocators.SIDE_BAR_MENU)

    def find_side_bar_menu_close_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.SIDE_BAR_MENU_CLOSE_BTN)

    def find_checkbox(self):
        return find_all_elements(self.wait, ExploreEphysPageLocators.CHECKBOX)

    def wait_for_element(self, locator):
        return find_visibility_of_all_elements(self.wait, locator)

    def check_filter_brain_region_title(self):
        return find_element(self.wait, ExploreEphysPageLocators.FILTER_BRAIN_REGION)

    def find_load_more_btn(self):
        return find_element(self.wait, ExploreEphysPageLocators.LOAD_MORE_BUTTON)

    def find_table_rows(self):
        return find_all_elements(self.wait, ExploreEphysPageLocators.TABLE_ROWS)

    def validate_empty_cells(self):
        rows = self.find_table_rows()
        for row_index, row in enumerate(rows, start=2):
            cells = find_all_elements(self.wait, ExploreEphysPageLocators.TABLE_CELLS)
            for cell_index, cell in enumerate(cells, start=2):
                if not cell.text.strip():
                    error_message = f'Error: Empty field in a row{row_index}, cell {cell_index}'
                    print(error_message)

    def perform_full_validation(self):
        self.validate_empty_cells()
        load_more_button = self.find_load_more_btn()
        load_more_button.click()

        self.validate_empty_cells()
