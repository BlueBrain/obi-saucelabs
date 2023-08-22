from selenium.webdriver.common.by import By


class ExploreNMorphologyPageLocators:
    NEURON_MORPHOLOGY_PAGE_TITLE = (By.XPATH, "//div[text()='Neuron morphology']")
    BRAIN_REGION_COLUMN = (By.XPATH, "//div[text()='Brain Region']/parent::div[@class='flex "
                                     "flex-col text-left']")
    MTYPE_COLUMN = (By.XPATH, "//div[text()='M-Type']/parent::div[@class='flex flex-col text-left']")
    NAME_COLUMN = (By.XPATH, "//div[text()='Name']/parent::div[@class='flex flex-col text-left']")
    SPECIES_COLUMN = (By.XPATH, "//div[text()='Species']/parent::div[@class='flex flex-col "
                                "text-left']")
    CONTRIBUTORS_COLUMN = (By.XPATH, "//div[text()='Contributors']/parent::div[@class='flex "
                                     "flex-col text-left']")
    CREATION_DATE_COLUMN = (By.XPATH, "//div[text()='Creation date']/parent::div[@class='flex "
                                      "flex-col text-left']")
    N_MORPHOLOGY_SIDE_BAR_EXPLORE_BTN = (
        By.XPATH, "//div[starts-with(@class,'sidebar_side')]//a[@href='/mmb-beta/explore' and "
                  "text()='Explore']")
    N_MORPHOLOGY_SIDE_BAR_PLUS_BTN = (
        By.XPATH, "//div[starts-with(@class,'sidebar_side')]//button[starts-with(@class, 'ant-btn "
                  "css')]")
    N_MORPHOLOGY_SIDE_BAR_MENU = (By.XPATH, "//aside/div[starts-with(@class,'sidebar_expanded__')]")
    N_MORPHOLOGY_HOME_BTN = (By.XPATH, "//span[@aria-label='home']/preceding-sibling::h2[text("
                                       ")='Home']")
    N_MORPHOLOGY_SIDE_BAR_MENU_CLOSE_BTN = (
        By.XPATH, "//button[@type='button' and starts-with(@class, 'ant-btn')]/span["
                  "@class='ant-btn-icon']")

