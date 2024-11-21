# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0


import json

from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import CustomBasePage
from util.util_links_checker import LinkChecker
from util.util_methods import click_element, find_element, assert_element_text
from util.util_scraper import UrlScraper


class HomePage(CustomBasePage, LinkChecker):

    def __init__(self, browser, wait):
        super().__init__(browser, wait)
        self.url_scraper = UrlScraper()

    def go_to_home_page(self):
        self.go_to_page("")

    def scrape_links(self):
        page_source = self.browser.page_source
        links = self.url_scraper.scrape_links(page_source)

    def find_login_button(self):
        return find_element(self.wait, HomePageLocators.LOGIN_BUTTON)
