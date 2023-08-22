from pages.explore_page import ExplorePage
from locators.explore_n_density_locators import ExploreNDensityPageLocators
from util.util_links_checker import LinkChecker
from util.util_methods import click_element, find_element, assert_element_text, find_all_elements
from util.util_scraper import UrlScraper


class ExploreNeuronDensityPage(ExplorePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = ExplorePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_neuron_density_page(self):
        self.browser.get(self.url + "/explore/neuron-density")
        return self.browser.current_url

    def find_contributors_column(self):
        return find_element(self.wait, ExploreNDensityPageLocators.CONTRIBUTORS_COLUMN)

    def find_empty_cells_in_contributors_column(self):
        contributors_column = self.find_contributors_column()
        cells = contributors_column.find_elements(*ExploreNDensityPageLocators.TABLE_CELLS)
        empty_cells = []
        for cell_index, cell in enumerate(cells, start=2):
            if not cell.text.strip():
                empty_cells.append((cell_index, cell))

        return empty_cells

    def find_load_more_btn(self):
        return find_element(self.wait, ExploreNDensityPageLocators.LOAD_MORE_BUTTON)

    def find_table_rows(self):
        return find_all_elements(self.wait, ExploreNDensityPageLocators.TABLE_ROWS)

    def validate_empty_cells_in_contributors(self):
        empty_cells = self.find_empty_cells_in_contributors_column()
        for cell_index, cell in empty_cells:
            error_message = f'Error: Empty field in cell {cell_index}'
            print(error_message)

    def perform_full_validation(self, max_load_more_clicks=5):
        for _ in range(max_load_more_clicks):
            self.validate_empty_cells_in_contributors()
            load_more_button = self.find_load_more_btn()
            load_more_button.click()
