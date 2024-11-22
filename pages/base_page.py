# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup", "logger")
class CustomBasePage:

    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait
        self.base_url = "https://openbluebrain.com/app"

    def go_to_page(self, page_url):
        url = self.base_url + page_url
        self.browser.get(url)

    def find_element(self, by_locator, timeout=10):
        return self.wait.until(EC.presence_of_element_located(by_locator), timeout)

    def element_visibility(self, by_locator, timeout=10):
        return self.wait.until(EC.visibility_of_element_located(by_locator), timeout)

    def visibility_of_all_elements(self, by_locator, timeout=10):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator), timeout)

    def find_all_elements(self, by_locator, timeout=10):
        return self.wait.until(EC.presence_of_all_elements_located(by_locator), timeout)

    def element_to_be_clickable(self, by_locator, timeout=10):
        self.wait.until(EC.element_to_be_clickable(by_locator), timeout)

    def assert_element_text(self, by_locator, expected_text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        assert element.text == expected_text

    def is_enabled(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.is_enabled()

    def enter_text(self, by_locator, text):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def wait_for_long_load(self, by_locator, timeout=60):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            self.wait.until(EC.visibility_of(element), timeout)

        except TimeoutException:
            print("Loading took too long")

    def wait_for_condition(self, condition, timeout=60, message=None):
        """
        General-purpose wait function to wait for a specific condition.
        :param condition: The condition to wait for (e.g., element presence, URL contains).
        :param timeout: How long to wait before timing out.
        :param message: Custom error message if timeout occurs.
        :return: The result of the condition (e.g., an element or True).
        """
        try:
            return self.wait.until(condition, message)
        except TimeoutException as e:
            raise RuntimeError(message or f"Condition not met within {timeout} seconds") from e