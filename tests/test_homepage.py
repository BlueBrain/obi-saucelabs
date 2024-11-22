# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import os.path
import time
import pytest
import requests

from pages.home_page import HomePage
from util.util_links_checker import LinkChecker
from util.util_links_writer import write_links_to_file
from util.util_load_links import LinkUtil
from util.util_scraper import UrlScraper

'''
Get the current working directory
Specify the relative path to the file from the current directory
Join the current directory with the relative file path
'''
current_directory = os.getcwd()
relative_file_path = 'scraped_links.txt'
file_path = os.path.join(current_directory, relative_file_path)


@pytest.mark.usefixtures("setup", "logger")
class TestFindLogin:
    @pytest.mark.run(order=2)
    def test_find_homepage_titles(self, setup, logger):
        home_page = HomePage(*setup)
        home_page.go_to_home_page()

    def test_find_login_button(self, setup, logger):
        home_page = HomePage(*setup)
        home_page.go_to_home_page()

        login_button = home_page.find_login_button()
        assert login_button.is_displayed()
        logger.info("'Log in' button is found")

    # def test_links(self):
    #     test_directory = os.path.dirname(os.path.abspath(__file__))
    #     links_file_path = os.path.join(test_directory, '..', 'links.json')
    #
    #     link_checker = LinkChecker()
    #     links = link_checker.load_links(links_file_path)['main_page_links']
    #     link_checker.check_links(links)
    #
    #     url = "https://openbluebrain.com/app"
    #     response = requests.get(url)
    #     page_source = response.text
    #     url_scraper = UrlScraper()
    #     scraped_links = url_scraper.scrape_links(page_source)
    #     write_links_to_file(file_path, scraped_links)
