import json
import logging
import os
import sys
import time
from io import BytesIO

import pytest
import urllib3
from PIL import Image
from selenium import webdriver
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.home_page import HomePage
from pages.login_page import LoginPage
from util.util_base import load_config

urllib3.disable_warnings()




@pytest.fixture(autouse=True)
def setup(request, pytestconfig):
    """Fixture to set up the browser/webdriver"""

    browser_name = os.environ.get("BROWSER_NAME")
    headless_mode = pytestconfig.getoption("--headless")
    browser = None
    options = ChromeOptions()  # Default to Chrome options

    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    options.headless = True

    sauce_options = {'username': os.environ["SAUCE_USERNAME"],
                     'accessKey': os.environ["SAUCE_ACCESS_KEY"],
                     'name': request.node.name}

    options.set_capability('sauce:options', sauce_options)
    sauce_url = "https://ondemand.eu-central-1.saucelabs.com/wd/hub"

    driver = webdriver.Remote(command_executor=sauce_url, options=options)

    yield driver

    if driver is not None:
        sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
        driver.execute_script("sauce:job-result={}".format(sauce_result))

        driver.quit()

@pytest.fixture()
def browser(request):
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'

    sauce_options = {'username': os.environ["SAUCE_USERNAME"],
                     'accessKey': os.environ["SAUCE_ACCESS_KEY"],
                     'name': request.node.name}

    options.set_capability('sauce:options', sauce_options)
    sauce_url = "https://ondemand.eu-central-1.saucelabs.com/wd/hub"

    browser = webdriver.Remote(command_executor=sauce_url, options=options)

    yield browser

    if browser is not None:
        sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
        browser.execute_script("sauce:job-result={}".format(sauce_result))

        browser.quit()



@pytest.fixture(scope="function")
def logger(request):
    """Fixture to initialize the logger object"""
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

    # Check if the logger already has a file handler
    has_file_handler = any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)
    # Check if the logger already has a stream handler

    has_stream_handler = any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers)
    # Determine the outer allure_reports directory
    allure_reports_dir = request.config.getoption("--alluredir")

    if not has_file_handler:
        # Create the outer allure_reports directory if it doesn't exist
        os.makedirs(allure_reports_dir, exist_ok=True)

        # Create the log file path
        log_file_path = os.path.join(allure_reports_dir, "report.log")

        # Create the log file handler
        file_handler = logging.FileHandler(filename=log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    if not has_stream_handler:
        # Create the stream handler for console output
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    return logger


@pytest.fixture(scope="function")
def navigate_to_login(setup):
    browser = setup
    wait = WebDriverWait(browser, 10)
    login_page = LoginPage(browser,wait)
    login_page.navigate_to_homepage()

    login_button = login_page.find_login_button()
    assert login_button.is_displayed()
    login_button.click()
    wait.until(EC.url_contains("auth"))
    return login_page


@pytest.fixture(scope="function")
def login(setup, navigate_to_login):
    """Fixture that navigates to the login page"""
    browser, wait = setup
    login_page = navigate_to_login
    config = load_config()
    username = config['username']
    password = config['password']

    if 'mmb-beta' not in browser.current_url:
        login_page.find_username_field().send_keys(username)
        login_page.find_password_field().send_keys(password)
        login_page.find_signin_button().click()
        wait.until(EC.url_contains("mmb-beta"))

    yield browser, wait
    login_page.browser.delete_all_cookies()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("Test failed - handling it")
            file_name = "latest_logs/" + report.nodeid.replace("::", "_") + ".png"
            if hasattr(item, "cls"):
                browser = getattr(item.cls, "browser", None)
            if not browser:
                browser = getattr(item, "_browser", None)
            if browser:
                print("Browser object found - making screenshot")
                _capture_screenshot(file_name, browser)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name, browser):
    os.makedirs(os.path.dirname(name), exist_ok=True)
    browser.get_full_page_screenshot_as_file(name)


# Hook to customize the HTML report table row cells
def pytest_html_results_table_row(report, cells):
    """Styling for html.report"""
    if report.failed:
        cells.insert(1, ("✘", "fail"))
    else:
        cells.insert(1, ("?", "skipped"))


def pytest_sessionstart(session):
    """ Hook to delete previous allure reports before running the tests"""
    folder_path = session.config.getoption("--alluredir")
    if os.path.exists(folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))


# Command-line options
def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        action="store",
        default="firefox",
        choices=["firefox"],
        help="Specify the browser to run the tests in",
    )

    parser.addoption("--log-file-path", action="store", default=None,
                     help="Specify the log file path")


def make_full_screenshot(browser, savename):
    """Performs a full screenshot of the entire page.
    Taken from https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    """
    logger.debug('Making full-page screenshot')
    # initiate value
    img_list = []  # to store image fragment
    offset = 0  # where to start

    # js to get height of the window
    try:
        height = browser.execute_script(
            "return Math.max("
            "document.documentElement.clientHeight, window.innerHeight);"
        )
    except exceptions.WebDriverException:
        return

    max_window_height = browser.execute_script(
        "return Math.max("
        "document.body.scrollHeight, "
        "document.body.offsetHeight, "
        "document.documentElement.clientHeight, "
        "document.documentElement.scrollHeight, "
        "document.documentElement.offsetHeight);"
    )

    header_height = 0
    while offset < max_window_height:
        browser.execute_script(f"window.scrollTo(0, {offset});")

        # get the screenshot of the current window
        img = Image.open(BytesIO((browser.driver.get_screenshot_as_png())))
        img_list.append(img)
        offset += height - header_height

    # Stitch image into one, set up the full screen frame
    img_frame_height = sum([img_frag.size[1] for img_frag in img_list])
    img_frame = Image.new("RGB", (img_list[0].size[0], img_frame_height))

    offset = 0  # offset used to create the snapshots
    img_loc = 0  # offset used to create the final image
    for img_frag in img_list:
        # image fragment must be cropped in case the page is a jupyter notebook;
        # also make sure the last image fragment gets added correctly to avoid overlap.
        offset1 = offset + height
        if offset1 > max_window_height:
            top_offset = offset + height - max_window_height
            box = (0, top_offset, img_frag.size[0], img_frag.size[1])
        else:
            box = (0, header_height, img_frag.size[0], img_frag.size[1])
        img_frame.paste(img_frag.crop(box), (0, img_loc))
        img_loc += img_frag.size[1] - header_height
        offset += height - header_height

    # Save the final image
    img_frame.save(savename)
