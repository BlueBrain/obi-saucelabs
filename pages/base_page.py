from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import CustomBasePageLocators
import pytest

@pytest.mark.usefixtures("setup", "logger")
class CustomBasePage:

    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait
        self.url = "https://bbp.epfl.ch/mmb-beta"


