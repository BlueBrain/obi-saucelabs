from selenium.webdriver.common.by import By


class CustomBasePageLocators:
    PAGE_LOAD = (By.XPATH, "//a[@href='https://bbp.epfl.ch/mmb-beta']")
