from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    SIGN_IN = (By.ID, 'kc-login')
    LOGOUT = (By.XPATH, '//button[text()="Logout"]')
    # ALREADY_LOGGED = (By.ID, "#kc-page-title") # cannot find this selector anymore


