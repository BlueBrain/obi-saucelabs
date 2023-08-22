from selenium.webdriver.common.by import By


class ExploreNDensityPageLocators:
    CONTRIBUTORS_COLUMN = (By.XPATH, "//div[text()='Contributors']/parent::div[@class='flex "
                                     "flex-col text-left']")

    LOAD_MORE_BUTTON = (By.XPATH, "//button[@type='button' and text()='Load 30 more results...']")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody.ant-table-tbody tr.ant-table-row")
    # TABLE_CELLS = (By.CSS_SELECTOR, "tbody.ant-table-tbody td.ant-table-cell")
    TABLE_CELLS = (
        By.CSS_SELECTOR,
        "tbody.ant-table-tbody td.ant-table-cell.text-primary-7.cursor-pointer.ant"
        "-table-cell-ellipsis")
