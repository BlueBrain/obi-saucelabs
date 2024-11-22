# Copyright (c) 2024 Blue Brain Project/EPFL
#
# SPDX-License-Identifier: Apache-2.0

from selenium.webdriver.common.by import By


class ExploreNDensityPageLocators:
    LOAD_MORE_BUTTON = (By.XPATH, "//button[@type='button' and text()='Load 30 more results...']")
    BRP_CEREBRUM = (By.XPATH, "//span[@title='Cerebrum' and text()='Cerebrum']")
    TABLE_ROWS = (By.CSS_SELECTOR, "tbody.ant-table-tbody tr.ant-table-row")
    TABLE_CELLS = (
        By.CSS_SELECTOR,
        "tbody.ant-table-tbody td.ant-table-cell.text-primary-7.cursor-pointer.ant"
        "-table-cell-ellipsis")
    NDENSITY_TAB = (By.XPATH, "//span[@class='ant-menu-title-content' and contains(text(),'Neuron "
                              "density')]")
    LV_THUMBNAIL = (By.XPATH, "//img[starts-with(@alt,'Morphology preview')]")
    LV_BRAIN_REGION = (By.XPATH, "//span[@class='ant-table-column-title']//div[text()='Brain "
                                 "Region']")
    LV_MTYPE = (By.XPATH, "//th[@data-testid='column-header']//div[text()='M-Type']")
    LV_ETYPE = (By.XPATH, "//th[@data-testid='column-header']//div[text()='E-Type']")
    LV_DENSITY = (By.XPATH, "//th[@data-testid='column-header']//div[contains(text(),'Density')]")
    LV_NMEASUREMENTS = (By.XPATH, "//th[@data-testid='column-header']//div[contains(text(),'N° of "
                                  "Measurements')]")
    LV_NAME = (By.XPATH, "//th[@data-testid='column-header']//div[text()='Name']")
    LV_SPECIES = (By.XPATH, "//th[@data-testid='column-header']//div[text()='Species']")
    LV_AGE = (By.XPATH, "//span[@class='ant-table-column-title']//div[contains(text(),'Age')]")
    LV_CONTRIBUTORS = (By.XPATH, "//th[@data-testid='column-header']//div[text()='Contributors']")
    LV_REGISTRATION_DATE = (By.XPATH, "//th[@data-testid='column-header']//div[text()='Creation "
                                      "Date']")
    LV_FILTER_MTYPE = (By.XPATH, "//span[text()='M-Type']")
    LV_BR_ROW1 = (By.XPATH, "(//td[starts-with(@class, 'ant-table-cell')])[13]")
    DV_DESC_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Description']")
    DV_CONTRIBUTORS_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                                       ")='Contributors']")
    DV_REG_DATE_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                                   ")='Registration date']")
    DV_BRAIN_REG_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Brain "
                                    "Region']")
    DV_LICENSE_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='License']")
    DV_SPECIES_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Species']")
    DV_NUM_MEAS_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='N° of "
                                   "Measurements']")
    DV_MTYPE_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='M-Type']")
    DV_ETYPE_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='E-Type']")
    DV_DENSITY_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Density']")
    DV_AGE_TITLE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Age']")
    DV_DOWNLOAD_BTN = (By.XPATH, "//div[text()='Download']")
    DV_DESC = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                         ")='Description']/following-sibling::div[@class='mt-2']")
    DV_BR_REG = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Brain "
                           "Region']/following-sibling::div[@class='mt-2']")
    DV_SPECIES = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                            ")='Species']/following-sibling::div[@class='mt-2']")
    DV_AGE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                        ")='Age']/following-sibling::div[@class='mt-2']")
    DV_DENSITY = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                            ")='Density']/following-sibling::div[@class='mt-2']")
    DV_NUM_MEAS = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='N° of "
                             "Measurements']/following-sibling::div[@class='mt-2']")
    DV_NAME = (By.XPATH, "//div[@class='text font-thin' and contains(text(), 'Name')]")
    DV_REG_DATE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text()='Registration "
                             "date']/following-sibling::div[@class='mt-2']")
    DV_CONTRIBUTORS = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                                 ")='Contributors']/following-sibling::div[@class='mt-2']")
    DV_LICENSE = (By.XPATH, "//div[@class='uppercase text-neutral-4' and text("
                            ")='License']/following-sibling::div[@class='mt-2']")

