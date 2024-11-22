# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

from locators.explore_ephys_locators import ExploreEphysLocators
from pages.explore_page import ExplorePage
from util.util_links_checker import LinkChecker
from util.util_scraper import UrlScraper


class ExploreElectrophysiologyPage(ExplorePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = ExplorePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_ephys_page(self):
        self.go_to_page("/explore/interactive/experimental/electrophysiology")

    def download_resources(self):
        return self.find_element(ExploreEphysLocators.DOWNLOAD_RESOURCES)

    def wait_for_element(self, locator):
        return self.visibility_of_all_elements(locator)

    def dv_id_plots(self):
        return self.find_element(ExploreEphysLocators.DV_ID_PLOTS)

    def dv_id_stimulus_title(self):
        return self.find_element(ExploreEphysLocators.DV_ID_STIMULUS_TITLE)

    def dv_id_repetition_title(self):
        return self.find_element(ExploreEphysLocators.DV_ID_REPETITION_TITLE)

    def dv_id_sweep_title(self):
        return self.find_element(ExploreEphysLocators.DV_ID_SWEEP_TITLE)

    def dv_interactive_details_btn(self):
        return self.find_element(ExploreEphysLocators.DV_INTER_DETAILS)

    def dv_overview_btn(self):
        return self.find_element(ExploreEphysLocators.DV_OVERVIEW)

    def dv_stimulus_btn(self):
        return self.find_element(ExploreEphysLocators.DV_STIMULUS_BTN)

    def dv_stimulus_all(self):
        return self.find_element(ExploreEphysLocators.DV_STIMULUS_ALL)

    def dv_stimulus_img_grid(self):
        return self.find_element(ExploreEphysLocators.DV_STIMULUS_IMG_GRID)

    def dv_stim_images(self):
        return self.find_all_elements(ExploreEphysLocators.DV_STIM_IMAGES)

    def find_apply_btn(self):
        return self.find_element(ExploreEphysLocators.APPLY_BTN)

    def find_btn_all_checkboxes(self):
        return self.find_element(ExploreEphysLocators.ALL_CHECKBOXES)

    def find_dv_metadata(self, locators):
        metadata = []
        for data in locators:
            metadata.extend(self.find_all_elements(data))
        return metadata

    def find_ephys_tab_title(self):
        return self.find_element(ExploreEphysLocators.EPHYS_TAB_TITLE)

    def filter_etype_btn(self):
        return self.find_element(ExploreEphysLocators.FILTER_ETYPE_BTN)

    def filter_etype_search(self):
        return self.find_element(ExploreEphysLocators.FILTER_ETYPE_SEARCH)

    def filter_etype_search_input(self):
        return self.find_element(ExploreEphysLocators.FILTER_ETYPE_SEARCH_INPUT)

    def filter_etype_input_type_area(self):
        return self.find_element(ExploreEphysLocators.FILTER_ETYPE_INPUT_TYPE_AREA)

    def find_filtered_etype(self):
        return self.find_all_elements(ExploreEphysLocators.FILTERED_ETYPE)

    def find_dv_title_header(self, title_locators):
        title_headers = []
        for title in title_locators:
            title_headers.extend(self.find_all_elements(title))
        return title_headers

    def find_column_headers(self, column_locators):
        column_headers = []
        for locator in column_locators:
            column_headers.extend(self.find_all_elements(locator))
        return column_headers

    def find_explore_section_grid(self):
        return self.element_visibility(ExploreEphysLocators.LV_GRID_VIEW)

    def find_filter_btn(self):
        return self.find_element(ExploreEphysLocators.LV_FILTER_BTN)

    def find_filter_close_btn(self):
        return self.element_visibility(ExploreEphysLocators.LV_FILTER_CLOSE_BTN)

    def find_load_more_btn(self):
        return self.find_element(self.wait, ExploreEphysLocators.LOAD_MORE_BUTTON)

    def find_table_rows(self):
        return self.find_all_elements(ExploreEphysLocators.TABLE_ROWS)

    def validate_empty_cells(self):
        rows = self.find_table_rows()
        for row_index, row in enumerate(rows, start=2):
            cells = self.find_all_elements(ExploreEphysLocators.TABLE_CELLS)
            for cell_index, cell in enumerate(cells, start=2):
                if not cell.text.strip():
                    error_message = f'Error: Empty field in a row{row_index}, cell {cell_index}'
                    print(error_message)

    def perform_full_validation(self):
        self.validate_empty_cells()
        load_more_button = self.find_load_more_btn()
        load_more_button.click()
        self.validate_empty_cells()

    def find_search_button(self):
        return self.find_element(ExploreEphysLocators.SEARCH_BUTTON)

    def find_search_input_search_item(self):
        return self.find_element(ExploreEphysLocators.SEARCH_INPUT_FIELD)

    def find_checkboxes(self):
        return self.find_all_elements(ExploreEphysLocators.CHECKBOXES)

    def find_table(self):
        return self.find_element(ExploreEphysLocators.TABLE)

    def find_thumbnails(self):
        return self.visibility_of_all_elements(ExploreEphysLocators.LV_THUMBNAIL)

    def lv_filter_apply(self):
        return self.find_element(ExploreEphysLocators.LV_FILTER_APPLY_BTN)

    def lv_row1(self):
        return self.find_element(ExploreEphysLocators.LV_ROW1)

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def search_species(self):
        return self.element_visibility(ExploreEphysLocators.SEARCHED_SPECIES)

    def verify_all_thumbnails_displayed(self):
        thumbnails = self.find_thumbnails()

        thumbnail_status = []
        for thumbnail in thumbnails:
            thumbnail_status.append({
                'element': thumbnail,
                'is_displayed': thumbnail.is_displayed()
            })

        return thumbnail_status

