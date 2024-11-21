from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(.,'Log in')]")
    LOGOUT = (By.XPATH, "//button[@type='button' and text()='Log out']")
    SIGN_IN = (By.XPATH, "//input[@type='submit']")
    USERNAME_FIELD = (By.XPATH, "//input[@id='username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    SUBMIT = (By.XPATH, "//input[@type='submit']")


