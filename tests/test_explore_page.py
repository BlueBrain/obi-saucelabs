# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import time
import os.path
import pytest
from locators.explore_page_locators import ExplorePageLocators
from pages.explore_page import ExplorePage


current_directory = os.getcwd()
relative_file_path = 'scraped_links.txt'
file_path = os.path.join(current_directory, relative_file_path)


class TestExplorePage:
    @pytest.mark.explore_page
    @pytest.mark.run(order=2)
    def test_explore_page(self, setup, login, logger, browser):
        """
        The commented out code below is pending changes in the platform.
        """
        browser, wait = setup
        explore_page = ExplorePage(browser, wait)
        explore_page.go_to_explore_page()
        logger.info("Explore page is loaded")

        """Checking the titles of the Explore Page"""
        explore_page.check_explore_title_is_present()
        logger.info("Explore page title is present")

        exp_data_titles = [
            ExplorePageLocators.NEURON_MORPHOLOGY,
            ExplorePageLocators.NEURON_ELECTROPHYSIOLOGY,
            ExplorePageLocators.NEURON_DENSITY,
            ExplorePageLocators.BOUTON_DENSITY,
            ExplorePageLocators.SYNAPSE_PER_CONNECTION
        ]
        logger.info("Searching for Experimental Data types")
        exp_data_titles = explore_page.find_experimental_data_titles(exp_data_titles)
        for title in exp_data_titles:
            assert title.is_displayed(), f"Experimental data {title} is not displayed."
        logger.info("Found Experimental data titles")

        page_titles = [
            ExplorePageLocators.EXPERIMENTAL_DATA_BTN,
            ExplorePageLocators.MODEL_DATA_BTN,
            ExplorePageLocators.LITERATURE
        ]
        logger.info("Searching for Explore Page titles")
        explore_page_titles = explore_page.find_explore_page_titles(page_titles)

        for page_title in explore_page_titles:
            assert page_title.is_displayed(), f"Explore page titles {page_title} is not displayed"
        logger.info("Found Explore page titles")
        logger.info("Verifying the records of the Experimental data types are present")
        record_count_locators = [
            ExplorePageLocators.MORPHOLOGY_NRECORDS,
            ExplorePageLocators.NEURON_EPHYS_NRECORDS,
            ExplorePageLocators.NEURON_DENSITY_NRECORDS,
            ExplorePageLocators.BOUTON_DENSITY_NRECORDS,
            ExplorePageLocators.SYNAPSE_PER_CONNECTION_NRECORDS
        ]
        record_counts = explore_page.get_experiment_record_count(record_count_locators)
        for record_count in record_counts:
            assert record_count >= 1, f"Record count is less than 100: {record_count}"
        logger.info("Number of records for data types are displayed")

        brain_region_panel = explore_page.find_brain_region_panel()
        logger.info("Found Brain Region Panel")

        cerebrum_in_brpanel = explore_page.find_cerebrum_brp()
        logger.info("Found Cerebrum in the brain region panel")

        cerebrum_arrow_btn = explore_page.find_cerebrum_arrow_btn()
        logger.info("Cerebrum - parent arrow button is clicked")
        browser.execute_script("arguments[0].click();",cerebrum_arrow_btn)

        cerebral_cortex_title = explore_page.find_cerebral_cortex_brp()
        logger.info("Found Cerebral cortex as a child of Cerebrum")

        neurons_panel = explore_page.find_neurons_panel()
        assert neurons_panel.is_displayed()
        logger.info("Neurons panel is displayed")

        density_count_switch = explore_page.find_count_switch()
        assert density_count_switch.is_displayed()
        logger.info("Density & count switch is displayed")

        atlas = explore_page.find_3d_atlas()
        assert atlas.is_displayed()
        logger.info("3D Atlas is displayed")

        atlas_fullscreen = explore_page.find_atlas_fullscreen_bt()
        logger.info("Found atlas fullscreen button")
        atlas_fullscreen.click()

        fulscreen_exit = explore_page.find_fullscreen_exit()
        logger.info("Fullscreen exit button is found")
        fulscreen_exit.click()
        logger.info("Fullscreen exit button is clicked, atlas is minimized")
