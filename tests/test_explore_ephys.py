# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import os
import time
import pytest
from selenium.webdriver import Keys
from locators.explore_ephys_locators import ExploreEphysLocators
from pages.explore_efys import ExploreElectrophysiologyPage
from util.util_links_checker import LinkChecker

current_directory = os.getcwd()
relative_file_path = 'scraped_links.txt'
file_path = os.path.join(current_directory, relative_file_path)


class TestExploreEphys:
    @pytest.mark.build_page
    @pytest.mark.run(order=4)
    def test_explore_ephys_page(self, setup, login, logger):
        browser, wait = setup
        explore_ephys_page = ExploreElectrophysiologyPage(browser, wait)
        time.sleep(2)
        explore_ephys_page.go_to_explore_ephys_page()
        ephys_tab_title = explore_ephys_page.find_ephys_tab_title()
        logger.info("'Electrophysiology' tab title is present.")

        lv_explore_grid = explore_ephys_page.find_explore_section_grid()
        logger.info("Explore section grid/table view is displayed")
        thumbnail_img = explore_ephys_page.verify_all_thumbnails_displayed()
        logger.info("Ephys thumbnail is displayed")

        column_locators = [
            ExploreEphysLocators.LV_PREVIEW,
            ExploreEphysLocators.LV_BRAIN_REGION,
            ExploreEphysLocators.LV_ETYPE,
            ExploreEphysLocators.LV_NAME,
            ExploreEphysLocators.LV_SPECIES,
        ]
        column_headers = explore_ephys_page.find_column_headers(column_locators)

        for header in column_headers:
            assert header.is_displayed(), f"Column header {header} is not displayed."
        logger.info("Found List View column headers.")

        all_checkbox = explore_ephys_page.find_btn_all_checkboxes()
        time.sleep(2)
        all_checkbox.click()
        logger.info("Select all checkbox is clicked all checkboxes ticked.")
        all_checkbox.click()
        logger.info("All the checkboxes are unchecked.")

        checkboxes = explore_ephys_page.find_checkboxes()
        checked_flag = False

        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
                logger.info("Checkbox was found and clicked successfully.")
            else:
                # Print the message only once if at least one checkbox was already checked
                if not checked_flag:
                    logger.info("At least one checkbox was already checked.")
                    checked_flag = True

        find_search_input = explore_ephys_page.find_search_input_search_item()
        logger.info("Search input field is found.")
        browser.execute_script("arguments[0].click();", find_search_input)

        find_search_input.send_keys("Rattus norvegicus")
        logger.info("Search input is searching for Rattus norvegicus")
        found_species = explore_ephys_page.search_species()
        text_found_species = found_species.text
        logger.info(f"Found searched species:{text_found_species}.")

        find_filter_btn = explore_ephys_page.find_filter_btn().click()
        logger.info("Listing view filter button is found and clicked.")

        filter_etype = explore_ephys_page.filter_etype_btn().click()
        logger.info("'E-Type' button inside filter is found and clicked.")

        filter_etype_search = explore_ephys_page.filter_etype_search()
        filter_etype_search.click()
        logger.info("Clicked on 'E-Type Search Field' in the filter.")
        filter_etype_search_input = explore_ephys_page.filter_etype_search_input()

        logger.info("Clicked on the ETYPE search field")
        filter_etype_search_input.send_keys("bNAC")
        logger.info("Enter 'bNAC' as a search parameter")
        filter_etype_search_input.send_keys(Keys.ENTER)
        logger.info("Key ENTER to confirm the searched ETYPE")

        logger.info("'bNAC' found.")
        apply = explore_ephys_page.find_apply_btn().click()
        logger.info("Clicked on text APPLY button.")

        lv_filter_apply_btn = explore_ephys_page.lv_filter_apply().click()
        logger.info("List view filter is applied.")
        find_filter_close_btn = explore_ephys_page.find_filter_close_btn().click()
        logger.info("Close listing view filter.")

        find_table = explore_ephys_page.find_table()
        filtered_etype = explore_ephys_page.find_filtered_etype()
        if filtered_etype:
            assert True
        else:
            print("Filtered Mtype cells cannot be found.")

        expected = "bNAC"
        value_found = any(expected in row.text for row in filtered_etype)
        assert value_found, (f'The value {expected} is not found in the table after applying the '
                             f'filter')

        lv_row1 = explore_ephys_page.lv_row1().click()
        logger.info("Clicked on row 1 to see 'Detail View'.")

        """The below is commented out, pending changes"""
        # title_locators = [
        #     ExploreEphysLocators.DV_CONTRIBUTORS_TITLE,
        #     ExploreEphysLocators.DV_ETYPE_TITLE,
        #     ExploreEphysLocators.DV_REG_DATE_TITLE,
        #     ExploreEphysLocators.DV_LICENSE_TITLE,
        #     ExploreEphysLocators.DV_BRAIN_REG_TITLE,
        #     ExploreEphysLocators.DV_SPECIES_TITLE,
        #     ExploreEphysLocators.DV_DESC_TITLE
        # ]
        #
        # title_headers = explore_ephys_page.find_dv_title_header(title_locators)
        # for title in title_headers:
        #     assert title.is_displayed(), f"DV title header {title} is not displayed"
        # logger.info("Verify the presence of title headers.")
        #
        # locators = [
        #     ExploreEphysLocators.DV_CONTRIBUTORS,
        #     ExploreEphysLocators.DV_ETYPE,
        #     ExploreEphysLocators.DV_REG_DATE,
        #     ExploreEphysLocators.DV_LICENSE,
        #     ExploreEphysLocators.DV_BR_REG,
        #     ExploreEphysLocators.DV_SPECIES,
        #     ExploreEphysLocators.DV_DESC
        # ]
        #
        # logger.info("Found metadata header locators.")
        # metadata_header = explore_ephys_page.find_dv_title_header(locators)
        # for data in metadata_header:
        #     assert data.is_displayed(), f"DV title header {data} is not displayed"
        # logger.info("Found detail view title headers.")
        #
        # dv_overview_btn = explore_ephys_page.dv_overview_btn()
        # logger.info("Found 'Overview' button.")
        # dv_interactive_details_btn = explore_ephys_page.dv_interactive_details_btn()
        # logger.info("Found 'Interactive details' button.")
        # dv_stimulus_btn = explore_ephys_page.dv_stimulus_btn().click()
        # logger.info("Clicked 'Stimulus dropdown' button.")
        # dv_stimulus_all = explore_ephys_page.dv_stimulus_all()
        # logger.info("All stimuli is displayed.")
        # dv_stimuli_images = explore_ephys_page.dv_stim_images()
        # assert dv_stimuli_images, "Stimuli plots are not displayed"
        # logger.info("Plots are displayed.")
        #
        # dv_interactive_details_btn.click()
        # logger.info("Clicked 'Interactive details' button.")
        # dv_id_plots = explore_ephys_page.dv_id_plots()
        # logger.info("Found 'Interactive detail' plots.")
        # dv_id_stimulus_title = explore_ephys_page.dv_id_stimulus_title()
        # logger.info("Found 'Interactive detail' Stimulus.")
        #
        # dv_id_repetition_title = explore_ephys_page.dv_id_repetition_title()
        # logger.info("Found 'Interactive detail' Repetition.")
        #
        # dv_id_sweep_title = explore_ephys_page.dv_id_sweep_title()
        # logger.info("Found 'Interactive detail' Sweep.")

    """The below is commented out, due to the changes in the platform"""
    # def test_links(self):
    """
    test_links methods checks the request status
    Also, writes non-dynamic URLs that are present on the page to a text file.
    """
    # test_directory = os.path.dirname(os.path.abspath(__file__))
    # links_file_path = os.path.join(test_directory, '..', 'links.json')
    #
    # link_checker = LinkChecker()
    # links = link_checker.load_links(links_file_path)['explore_ephys_links']
    # link_checker.check_links(links)
