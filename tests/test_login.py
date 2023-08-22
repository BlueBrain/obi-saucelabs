from util.util_base import load_config
import pytest
import time


class TestLogin:
    @pytest.mark.run(order=1)
    def test_login_process(self, setup, logger, navigate_to_login):
        """Test the login process"""
        try:
            login_page = navigate_to_login
            username_field = login_page.find_username_field()
            assert username_field.is_displayed()
            logger.info('The username field is displayed')
            username_field.send_keys(load_config()['username'])

            password_field = login_page.find_password_field()
            assert password_field.is_displayed()
            logger.info('The password field is displayed')
            password_field.send_keys(load_config()['password'])

            sign_in_button = login_page.find_signin_button()
            assert sign_in_button.is_displayed()
            sign_in_button.click()
            logger.info('The SIGN IN button clicked')

            login_page.wait_for_login_complete()  # Wait for login to complete

            logout_button = login_page.find_logout_button()
            assert logout_button.text == 'Logout'
            assert logout_button.is_displayed()

        except AssertionError as assertion_error:
            logger.error(f"Assertion Error: {assertion_error}")
            raise

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise


