from selenium.webdriver.common.by import By


class ExploreEphysPageLocators:
    NEURON_EPHYS_PAGE_TITLE = (By.XPATH, "//div[contains(text(),'Neuron electrophysiology')]")
    # SEARCH_LABEL = (By.XPATH, "//span[contains(@class, 'anticon-search') and
    # @aria-label='search']")
    SEARCH_BUTTON = (By.XPATH, "//span[@aria-label='search']/parent::button[@type='button']")
    # SEARCH_INPUT_FIELD = (By.XPATH, "//span[starts-with(@class,'ant-input-affix-wrapper
    # ant-input-affix-wrapper-lg')]/input[@type='text' and starts-with(@class,'ant-input
    # ant-input-lg')]")
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Type your search...']")
    BRAIN_REGION_COLUMN = (By.XPATH, "//div[text()='Brain Region']")
    E_TYPE_COLUMN = (By.XPATH, "//div[text()='E-Type']")
    NAME_REGION_COLUMN = (By.XPATH, "//div[text()='Name']")
    SPECIES_REGION_COLUMN = (By.XPATH, "//div[text()='Species']")
    CONTRIBUTORS_COLUMN = (By.XPATH, "//div[text()='Contributors']")
    CREATION_DATE_COLUMN = (By.XPATH, "//div[text()='Creation date']")
    CLEAR_FILTERS_BTN = (By.XPATH, "//button[@type='button']/span[text()='Clear filters']")
    FILTER_BTN = (
    By.XPATH, "//span[text()='Filters']/parent::div[@class='flex gap-3 items-center']")
    FILTER_CLOSE_BTN = (
    By.XPATH, "//button[@type='button']/span[@role='img' and @class='anticon anticon-close']")
    SIDE_BAR_EXPLORE_BTN = (
        By.XPATH,
        "//div[starts-with(@class,'sidebar_side')]//a[@href='/mmb-beta/explore' and text("
        ")='Explore']")
    SIDE_BAR_PLUS_BTN = (
        By.XPATH, "//div[starts-with(@class,'sidebar_side')]//button[starts-with(@class, 'ant-btn "
                  "css')]")
    SIDE_BAR_MENU = (By.XPATH, "//aside/div[starts-with(@class,'sidebar_expanded__')]")
    SIDE_BAR_MENU_CLOSE_BTN = (
        By.XPATH, "//button[@type='button' and starts-with(@class, 'ant-btn')]/span["
                  "@class='ant-btn-icon']")
    CHECKBOX = (By.CSS_SELECTOR, "tbody input.ant-checkbox-input")
    FILTER_BRAIN_REGION = (By.XPATH, "//span[text()='Brain Region']//ancestor::div["
                                     "@class='divide-y divide-primary-7 flex flex-col space-y-5' "
                                     "and @data-orientation='vertical']")
    FILTER_E_TYPE = (By.XPATH, "//span[text()='E-Type']//ancestor::div[@class='divide-y "
                               "divide-primary-7 flex flex-col space-y-5' and "
                               "@data-orientation='vertical']")
    FILTER_NAME = (By.XPATH, "//span[text()='Name']//ancestor::div[@class='divide-y "
                             "divide-primary-7 flex flex-col space-y-5' and "
                             "@data-orientation='vertical']")
    FILTER_SPECIES = (By.XPATH, "//span[text()='Species']//ancestor::div[@class='divide-y "
                                "divide-primary-7 flex flex-col space-y-5' and "
                                "@data-orientation='vertical']")
    FILTER_CONTRIBUTOR = (By.XPATH, "//span[text()='Contributors']//ancestor::div["
                                    "@class='divide-y divide-primary-7 flex flex-col space-y-5' "
                                    "and @data-orientation='vertical']")
    FILTER_CREATION_DATE = (By.XPATH, "//span[text()='Creation date']//ancestor::div["
                                      "@class='divide-y divide-primary-7 flex flex-col space-y-5' "
                                      "and @data-orientation='vertical']")
    LOAD_MORE_BUTTON = (By.XPATH, "//button[@type='button' and text()='Load 30 more results...']")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody.ant-table-tbody tr.ant-table-row")
    # TABLE_CELLS = (By.CSS_SELECTOR, "tbody.ant-table-tbody td.ant-table-cell")
    TABLE_CELLS = (By.CSS_SELECTOR, "tbody.ant-table-tbody "
                                    "td.ant-table-cell.text-primary-7.cursor-pointer.ant-table"
                                    "-cell-ellipsis")
