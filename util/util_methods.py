from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def find_element(wait, by_locator, timeout=10):
    return wait.until(EC.presence_of_element_located(by_locator), timeout)


def find_element_visibility(wait, by_locator, timeout=10):
    return wait.until(EC.visibility_of_element_located(by_locator), timeout)


def find_visibility_of_all_elements(wait, by_locator, timeout=10):
    return wait.until(EC.visibility_of_all_elements_located(by_locator), timeout)


def find_all_elements(wait, by_locator, timeout=10):
    return wait.until(EC.presence_of_all_elements_located(by_locator), timeout)


def click_element(wait, by_locator):
    wait.until(EC.element_to_be_clickable(by_locator)).click()


def assert_element_text(wait, by_locator, expected_text):
    element = wait.until(EC.visibility_of_element_located(by_locator))
    assert element.text == expected_text


def is_enabled(wait, by_locator):
    element = wait.until(EC.visibility_of_element_located(by_locator))
    return element.is_enabled()


def enter_text(wait, by_locator, text):
    return wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)


def is_visible(wait, by_locator):
    element = wait.until(EC.visibility_of_element_located(by_locator))
    return bool(element)


def wait_for_long_load(wait, by_locator, timeout=60):
    try:
        element = wait.until(EC.presence_of_element_located(by_locator))
        wait.until(EC.visibility_of(element))
        # Add more conditions as needed

    except TimeoutException:
        print("Loading took too long")