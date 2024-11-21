# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(.,'Log in')]")
