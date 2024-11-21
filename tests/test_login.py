from util.util_base import load_config
import pytest
import time


@pytest.mark.usefixtures("setup", "logger", "login")
class TestLogin:
    @pytest.mark.run(order=1)
    def test_login_process(self, setup, logger, browser):
        """Test the login process"""
        browser, wait = setup
        # Validate the user is logged in
        print("Login process completed via fixture")
        assert "app/explore" in browser.current_url, \
            f"Unexpected URL after login: {browser.current_url}"

        logger.info(f"Successfully logged in. Current page URL: {browser.current_url}")

