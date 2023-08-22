import os
import time
import pytest
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
        ephys_page = explore_ephys_page.go_to_explore_ephys_page()
        assert ephys_page == "https://bbp.epfl.ch/mmb-beta/explore/electrophysiology"

        find_ephys_page_title = explore_ephys_page.find_ephys_page_title()
        logger.info("Neuron electrophysiology title is present")
        find_ephys_brain_region_c_header = explore_ephys_page.find_brain_region_header()
        logger.info("Electrophysiology 'Brain region' column header")
        find_ephys_e_type_c_header = explore_ephys_page.find_e_type_header()
        logger.info("Electrophysiology 'E_Type' column header")
        find_ephys_name_c_header = explore_ephys_page.find_name_header()
        logger.info("Electrophysiology 'Name' column header")
        find_ephys_species_c_header = explore_ephys_page.find_species_header()
        logger.info("Electrophysiology 'Species' column header")
        find_ephys_contributors_c_header = explore_ephys_page.find_contributors_header()
        logger.info("Electrophysiology 'Contributors' column header")
        find_ephys_date_c_header = explore_ephys_page.find_creation_date_header()
        logger.info("Electrophysiology 'Creation date' column header")

        try:
            # Find all checkboxes on the page
            checkboxes = explore_ephys_page.find_checkbox()

            # Click on the first 5 checkboxes
            for checkbox in checkboxes[:5]:
                checkbox.click()
                logger.info("Clicked on checkbox")

            # Uncheck the checkboxes after the first 5
            for checkbox in checkboxes[:5]:
                if checkbox.is_selected():
                    checkbox.click()
                    logger.info("Unchecked checkbox")

        except Exception as e:
            print("An error occurred:", e)

        validate_table_fields = explore_ephys_page.perform_full_validation()
        logger.info("Table validation for checking empty fields is performed")
        find_search_field = explore_ephys_page.find_search_button()
        assert find_search_field is not None
        logger.info("Search field is found")
        find_search_field.click()

        find_search_input = explore_ephys_page.find_search_input_search_item()
        find_search_input.send_keys("Mus muculus")
        logger.info("Search input for Species")

        find_filter_btn = explore_ephys_page.find_filter_btn().click()
        logger.info("Looking for filter button")

        filter_brain_region = explore_ephys_page.check_filter_brain_region_title()
        filter_brain_region_txt = filter_brain_region.text
        print("Filter titles", filter_brain_region_txt)

        find_filter_close_btn = explore_ephys_page.find_filter_close_btn().click()
        logger.info("Looking for filter close button")

        find_side_bar_plus_icon = explore_ephys_page.find_side_bar_plus_btn().click()
        logger.info("Looking for side bar plus icon")

        find_side_bar_menu = explore_ephys_page.find_side_bar_menu()
        logger.info("Side bar menu is open")

        find_side_bar_menu_close_btn = explore_ephys_page.find_side_bar_menu_close_btn()
        logger.info("Side bar menu close")
        find_side_bar_menu_close_btn.click()
        logger.info("Side bar menus is clicked to close")

    def test_links(self):
        """
        test_links methods checks the request status
        Also, writes non-dynamic URLs that are present on the page to a text file.
        """
        test_directory = os.path.dirname(os.path.abspath(__file__))
        links_file_path = os.path.join(test_directory, '..', 'links.json')

        link_checker = LinkChecker()
        links = link_checker.load_links(links_file_path)['explore_ephys_links']
        link_checker.check_links(links)
