# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

from pages.explore_page import ExplorePage
from locators.explore_morphology_locators import ExploreMorphologyPageLocators
from util.util_links_checker import LinkChecker
from util.util_scraper import UrlScraper


class ExploreMorphologyPage(ExplorePage, LinkChecker):
    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.home_page = ExplorePage(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_explore_morphology_page(self):
        self.go_to_page("/explore/interactive/experimental/morphology")
        print("pages/morphology: ", self.browser.current_url)

    def find_morphology_tab(self):
        return self.find_element(ExploreMorphologyPageLocators.MORPHOLOGY_TAB)

    def morphology_filter(self):
        return self.element_visibility(ExploreMorphologyPageLocators.MORPHOLOGY_FILTER)

    def morphology_filter_close_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.MORPHOLOGY_FILTER_CLOSE_BTN)

    def find_column_headers(self, column_locators):
        column_headers = []
        for locator in column_locators:
            column_headers.extend(self.find_all_elements(locator))
        return column_headers

    def find_thumbnails(self):
        return self.find_all_elements(ExploreMorphologyPageLocators.LV_THUMBNAIL)

    def verify_all_thumbnails_displayed(self):
        thumbnails = self.find_thumbnails()

        thumbnail_status = []
        for thumbnail in thumbnails:
            thumbnail_status.append({
                'element': thumbnail,
                'is_displayed': thumbnail.is_displayed()
            })

        return thumbnail_status

    def find_results(self):
        return self.find_element(ExploreMorphologyPageLocators.RESULTS)

    def find_br_sort_arrow(self):
        return self.element_visibility(ExploreMorphologyPageLocators.BR_SORT_ARROW)

    def find_br_sorted(self):
        return self.element_visibility(ExploreMorphologyPageLocators.BR_SORTED)

    def find_species_sorted(self):
        return self.element_visibility(ExploreMorphologyPageLocators.SPECIES_SORTED)

    def find_first_row(self):
        return self.element_visibility(ExploreMorphologyPageLocators.FIRST_ROW)

    def find_table(self):
        return self.find_element(ExploreMorphologyPageLocators.TABLE)

    def get_table_data(self):
        table = self.find_element(ExploreMorphologyPageLocators.TABLE)
        rows = self.find_all_elements(ExploreMorphologyPageLocators.ROW)

        table_data = []
        for row in rows:
            cells = self.find_all_elements(ExploreMorphologyPageLocators.CELLS)
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

    def is_sorted(self, data):
        # Check if data is not None and has at least one row
        if data and len(data) > 0 and data[0] is not None:
            for col_index in range(len(data[0])):
                col_values = [row[col_index] for row in data]
                if col_values != sorted(col_values):
                    return False
            return True
        else:
            return False

    def find_back_to_ie_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.BACK_IE_BTN)

    def find_dv_headers(self, dv_header_locators):
        result_list = []
        for locator in dv_header_locators:
            result_list.extend(self.find_all_elements(locator))
        return result_list

    def confirm_selected_br(self):
        return self.find_element(ExploreMorphologyPageLocators.DV_SELECTED_BR)

    def find_morphometrics_title(self):
        return self.find_element(ExploreMorphologyPageLocators.DV_MORPHOMETRICS_TITLE)

    def find_morphology_titles(self, morpho_title):
        morpho_title = []
        for title in morpho_title:
            morpho_title.extend(self.find_all_elements(title))
        return morpho_title

    def find_morpho_viewer(self):
        return self.find_element(ExploreMorphologyPageLocators.MORPHO_VIEWER)

    def find_fullscreen_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.MORPHO_VIEWER_FULLSCREEN_BTN)

    def morpho_viewer_settings_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.MORPHO_VIEWER_SETTINGS_BTN)

    def find_download_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.DV_DOWNLOAD_BTN)

    def find_back_to_list_btn(self):
        return self.element_visibility(ExploreMorphologyPageLocators.DV_BACK_BTN)

    def filter_mtype(self):
        return self.element_visibility(ExploreMorphologyPageLocators.LV_FILTER_MTYPE)

    def filter_mtype_search(self):
        return self.find_element(ExploreMorphologyPageLocators.FILTER_MTYPE_SEARCH)

    def filter_mtype_text_input(self):
        return self.find_element(ExploreMorphologyPageLocators.FILTER_MTYPE_TEXT_INPUT)

    def lv_filter_apply(self):
        return self.find_element(ExploreMorphologyPageLocators.LV_FILTER_APPLY_BTN)

    def find_filtered_mtype(self):
        return self.find_all_elements(ExploreMorphologyPageLocators.FILTERED_MTYPE)

    def find_search_input_search_item(self):
        return self.find_element(ExploreMorphologyPageLocators.SEARCH_INPUT_FIELD)

    def search_name(self):
        return self.element_visibility(ExploreMorphologyPageLocators.SEARCH_NAME)

    def clear_filters_btn(self):
        return self.find_element(ExploreMorphologyPageLocators.CLEAR_FILTERS_BTN)