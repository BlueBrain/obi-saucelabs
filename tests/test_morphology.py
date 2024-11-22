# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.explore_morphology_locators import ExploreMorphologyPageLocators
from pages.explore_morphology import ExploreMorphologyPage


class TestExploreMorphologyPage:
    @pytest.mark.explore_page
    @pytest.mark.run(order=3)
    def test_explore_morphology(self, setup, login, logger):
        browser, wait = setup
        explore_morphology = ExploreMorphologyPage(browser, wait)
        print(f'MORPH URL:', browser.current_url)
        explore_morphology.go_to_explore_morphology_page()
        logger.info("Explore morphology page is displayed")
        morphology_tab = explore_morphology.find_morphology_tab()
        logger.info("Morphology tab is displayed")

        column_locators = [
            ExploreMorphologyPageLocators.LV_PREVIEW,
            ExploreMorphologyPageLocators.LV_BRAIN_REGION,
            ExploreMorphologyPageLocators.LV_MTYPE,
            ExploreMorphologyPageLocators.LV_NAME,
            ExploreMorphologyPageLocators.LV_SPECIES,
        ]
        column_headers = explore_morphology.find_column_headers(column_locators)

        for header in column_headers:
            assert header.is_displayed(), f"Column header {header} is not displayed."
        logger.info("Morphology column headers are displayed")

        thumbnail_img = explore_morphology.verify_all_thumbnails_displayed()
        logger.info("Morphology thumbnail is displayed")

        results = explore_morphology.find_results()
        logger.info("Total number of results for morphology tab is displayed")

        # try:
        #     br_sort_arrow = explore_morphology.find_br_sort_arrow()
        #     logger.info("Found the sorting arrow of Brain region column")
        #     # The wait is required to wait for the thumbnails to load
        #     time.sleep(5)
        #     br_sort_arrow.click()
        #     logger.info("The arrow to sort the brain region is clicked")
        # except TimeoutException:
        #     print("Timed out waiting for page to load")
        #     logger.info("The column header arrow was not found")

        # find_table = explore_morphology.find_table()
        # sorted_table_data = explore_morphology.get_table_data()
        # assert explore_morphology.is_sorted(sorted_table_data), "Table is not sorted as expected"

        morphology_filter = explore_morphology.morphology_filter()
        morphology_filter.click()
        logger.info("Filter is toggled open")

        filter_mtype = explore_morphology.filter_mtype()
        logger.info("In the filter Mtype button is displayed")
        filter_mtype.click()
        logger.info("In the filter Mtype button is clicked")
        time.sleep(2)

        filter_mtype_search = explore_morphology.filter_mtype_search()
        logger.info("In the filter Mtype Search Field is found")
        filter_mtype_search.click()
        logger.info("In the filter Mtype Search Field is CLICKED")

        filter_mtype_text_input = explore_morphology.filter_mtype_text_input()
        if filter_mtype_text_input:
            assert True
            logger.info("Text input field is found")
        else:
            print("input_id is not valid or cannot be found")
        filter_mtype_text_input.click()
        logger.info("Text input field is CLICKED")
        filter_mtype_text_input.send_keys("L5_TPC:A")
        logger.info("Looking for L5_TPC:A")
        filter_mtype_text_input.send_keys(Keys.ENTER)
        logger.info("L5_TPC:A is typed in the search field")

        lv_filter_apply_btn = explore_morphology.lv_filter_apply()
        logger.info("Inside the filter 'Apply' button is FOUND")
        lv_filter_apply_btn.click()
        logger.info("Inside the filter 'Apply' button is CLICKED")

        close_filter = explore_morphology.morphology_filter_close_btn()
        logger.info("Find button to close the filter")
        close_filter.click()
        logger.info("Filter panel is CLOSED")

        find_table = explore_morphology.find_table()
        filtered_mtype = explore_morphology.find_filtered_mtype()
        if filtered_mtype:
            assert True
        else:
            print("Filtered Mtype cells cannot be found")

        expected = "L5_TPC:A"
        value_found = any(expected in row.text for row in filtered_mtype)
        assert value_found, (f'The value {expected} is not found in the table after applying the '
                             f'filter')

        morphology_filter = explore_morphology.morphology_filter()
        morphology_filter.click()
        logger.info("Filter is toggled open")
        clear_filters_btn = explore_morphology.clear_filters_btn().click()

        find_search_input = explore_morphology.find_search_input_search_item()
        logger.info("Search input field is found")
        browser.execute_script("arguments[0].click();", find_search_input)

        find_search_input.send_keys("mtC070301B_idC")
        logger.info("Search input is searching for 'mtC070301B_idC'")
        found_name = explore_morphology.search_name()
        text_found_name = found_name.text
        logger.info(f"Found searched species:{text_found_name}")
        found_name.click()
        logger.info("Clicked on the researched name")

        dv_header_locators = [
            ExploreMorphologyPageLocators.DV_BRAIN_REGION,
            ExploreMorphologyPageLocators.DV_NAME,
            ExploreMorphologyPageLocators.DV_SPECIES,
            ExploreMorphologyPageLocators.DV_DESCRIPTION,
            ExploreMorphologyPageLocators.DV_CONTRIBUTORS,
            ExploreMorphologyPageLocators.DV_REGISTRATION_DATE,
            ExploreMorphologyPageLocators.DV_LICENSE,
        ]
        logger.info("Found 'Detail view' header locators.")
        dv_header_locators = explore_morphology.find_dv_headers(dv_header_locators)

        for header in dv_header_locators:
            assert header.is_displayed(), f"Detail view header {header} is not displayed."
        logger.info("Found detail view headers")

        # confirm_selected_br = explore_morphology.confirm_selected_br()
        # selected_br = confirm_selected_br.text
        # assert selected_br == "Anterior cingulate area, dorsal part, layer 2/3"
        # logger.info("Detail view selected brain region verified")

        morphometrics_title = explore_morphology.find_morphometrics_title()
        morpho_title = morphometrics_title.text
        assert morpho_title == "Morphometrics"

        morphology_titles = [
            ExploreMorphologyPageLocators.DV_NM_TITLE,
            ExploreMorphologyPageLocators.DV_AXON_TITLE,
            ExploreMorphologyPageLocators.DV_BD_TITLE,
            ExploreMorphologyPageLocators.DV_AP_TITLE,
            ExploreMorphologyPageLocators.DV_SOMA_TITLE
        ]
        logger.info("Found 'Detail view' titles.")
        morphology_titles = explore_morphology.find_morphology_titles(morphology_titles)

        for title in morphology_titles:
            assert title.is_displayed(), f"Detail view Morphology title:  {title} is not displayed."
        logger.info("Found detail view morphology titles")

        morpho_viewer = explore_morphology.find_morpho_viewer()
        logger.info("Morphology viewer is displayed")
        morpho_fullscreen_btn = explore_morphology.find_fullscreen_btn()
        logger.info("Morphology viewer full screen button is displayed")
        morpho_fullscreen_btn.click()
        logger.info("Click to view morphology full screen")
        morpho_viewer_settings_btn = explore_morphology.morpho_viewer_settings_btn()
        morpho_viewer_settings_btn.click()
        logger.info("Morphology viewer settings button clicked")
        morpho_fullscreen_btn.click()
        logger.info("Close full screen")
        download_btn = explore_morphology.find_download_btn()
        logger.info("Morphology 'Download' button is displayed")

        try:
            back_btn = explore_morphology.find_back_to_list_btn()
            browser.execute_script("arguments[0].scrollIntoView(true);", back_btn)
            logger.info("Found the Back button to go back to list view")
            # 1 sec delay is necessary to ensure scrolling is complete
            time.sleep(1)
            back_btn.click()
            logger.info("'Back to list' button to go back to list view is clicked.")
        except TimeoutException:
            print("Timed out waiting for page to load")
            logger.info("The 'Back to list' button was not displayed.")

        back_to_ie = explore_morphology.find_back_to_ie_btn()
        logger.info("Back to Interactive exploration button found.")
        back_to_ie.click()
        logger.info("Returned to the Interactive exploration page.")
