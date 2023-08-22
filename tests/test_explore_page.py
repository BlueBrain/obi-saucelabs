import time
import os.path
import pytest
import requests

from pages.explore_page import ExplorePage
from util.util_links_checker import LinkChecker

current_directory = os.getcwd()
relative_file_path = 'scraped_links.txt'
file_path = os.path.join(current_directory, relative_file_path)


class TestExplorePage:
    @pytest.mark.explore_page
    @pytest.mark.run(order=3)
    def test_explore_page(self, setup, login, logger):
        browser, wait = setup
        explore_page = ExplorePage(browser, wait)
        exp_url = explore_page.go_to_explore_page()
        assert exp_url == "https://bbp.epfl.ch/mmb-beta/explore"
        logger.info("Explore page is loaded")

        # Checking the titles of the Explore Page
        check_explore_title = explore_page.check_explore_title_is_present()
        logger.info("Explore page title is present")

        brain_models_title = explore_page.brain_models_title()
        brain_txt = brain_models_title.text
        logger.info("Brain models title is found")

        simulations_title = explore_page.simulations_title()
        simul = simulations_title.text
        print(simul, "CHECKING SIMULATIONS")
        logger.info("Verifying 'Simulations' title is found")

        experimental_data_title = explore_page.experimental_data_title()
        exp_data = experimental_data_title.text
        logger.info("Verifying 'Experimental data' title is found")

        portals_title = explore_page.portals_title()
        portal_txt = portals_title.text
        logger.info("Verifying 'Portals' title is found")

        gallery_title = explore_page.gallery_title()
        gallery_txt = gallery_title.text
        logger.info("Verifying 'Gallery' title is found")

        literature_title = explore_page.literature_title()
        literature_txt = literature_title.text
        logger.info("Verifying 'Literature' title is found")

        click_experimental_data = explore_page.experimental_data_button()
        logger.info("Selecting 'Experimental Data' section")
        # time.sleep(5)
        click_experimental_data.click()

        experimental_data_links = [
            explore_page.neuron_electrophysiology_link(),
            explore_page.neuron_morphology_link(),
            explore_page.bouton_density_link(),
            explore_page.neuron_density_link(),
            explore_page.layer_thickness_link(),
            explore_page.synapse_per_connection_link()
        ]

        exp_data_titles = [
            "Neuron electrophysiology link:",
            "Neuron morphology href:",
            "Bouton density href:",
            "Neuron density href:",
            "Layer thickness href:",
            "Synapse per connection href:"
        ]

        for link, title in zip(experimental_data_links, exp_data_titles):
            href_value = link.get_attribute('href')
            print(title, href_value)

        explore_page_links = [
            explore_page.brain_models_links(),
            explore_page.simulations_link()
        ]

        titles = [
            "Brain models link:",
            "Simulations link:"
        ]

        for link, title in zip(explore_page_links, titles):
            href_value = link.get_attribute('href')
            print(title, href_value)

    def test_links(self):
        """
        test_links methods checks the request status
        Also, writes non-dynamic URLs that are present on the page to a text file.
        """
        test_directory = os.path.dirname(os.path.abspath(__file__))
        links_file_path = os.path.join(test_directory, '..', 'links.json')

        link_checker = LinkChecker()
        links = link_checker.load_links(links_file_path)['explore_page_links']
        link_checker.check_links(links)
        # url = "https://bbp.epfl.ch/mmb-beta/explore/electrophysiology"
        # response = requests.get(url)
        # page_source = response.text
        # print(page_source, "THIS IS FROM THE EXPLORE_TEST, PAGE_LINKS")
        # url_scraper = UrlScraper()
        # scraped_links = url_scraper.scrape_links(page_source)
        #
        # write_links_to_file(file_path, scraped_links)
        # # print("Scraped links from Explore page saved to file successfully")
        # print("File path EXPLORE test", file_path)
        # print("Scraped links EXPLORE page", scraped_links)
