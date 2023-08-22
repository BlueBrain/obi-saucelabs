from selenium.webdriver.common.by import By


class BuildPageLocators:
    RECENT_CONFIGURATIONS = (By.XPATH, "//h3[contains(text(), 'Recently used configurations')]")
    RELEASE_VERSION = (By.XPATH, "//div[contains(text(), 'Release 23.01')]")
    PUBLIC_CONFIG_RELEASE = (By.XPATH, "//tbody//tr//*[contains(text(),'Release 23.01')]")
    BUILD_PAGE_CLICK_PLUS_ICON = (By.CSS_SELECTOR, "svg.icon_icon__TwrM_ > path")
    BASIC_CELL_GROUPS_REGIONS = (By.XPATH, "//span[text()='Basic cell groups and regions']")
    CONFIG_SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Search brain configuration...']")
    CUSTOM_MODEL_CONFIG = (By.XPATH, "//td[@class='ant-table-cell' and contains(text(), 'Custom "
                                     "model configuration.')]")
    BTN_CLONE_CONFIG = (
    By.XPATH, "//tr[2]/td[contains(text(), 'Custom model "
              "configuration')]/following-sibling::td//button[2]")
    EDIT_MODAL = (By.CSS_SELECTOR, 'div[role="dialog"][aria-modal="true"]')
    EDIT_CONFIG_DIALOG = (By.XPATH, "//div[@role='dialog' and @aria-modal='true']//div["
                                    "@class='ant-modal-confirm-body']//span[text()='Edit "
                                    "configuration']")
    CONFIG_TEXT_FIELD_NAME = (By.CSS_SELECTOR, '#name')
    CHANGE_CONFIG_NAME_TEXT_FIELD = (By.CSS_SELECTOR, "#name")
    DESCRIPTION = (By.ID, 'description')
    BTN_START_EDITING = (By.XPATH, "//span[text()='Start editing']")
    BASIC_CELL_GROUPS_AND_REGIONS = (By.XPATH, "//span[contains(text(),'Basic cell groups and "
                                               "regions')]")
    BUILD_AND_SIMULATE_BUTTON = (By.XPATH, "//div[@class='flex']/button[@type='button' and text("
                                           ")='Build & Simulate']")
    BRAIN_BUILD_SECTION_MAIN = (By.XPATH, "//*[starts-with(@class,'build-section-main_')]")
    BRAIN_BUILD_CLOSED_DIV = (By.XPATH, "//div[@data-state='closed']")
    VISIBLE_BASIC_CELL_GROUPS_TEXT = (By.XPATH, "//span[text()='Basic cell groups and regions']")
    BASIC_CELL_GROUPS_ARROW_BTN = (
    By.XPATH, "//div[@class='py-3 flex items-center justify-between']//button[3]//*[name()='svg']")
    BRAIN_STEM_BTN = (By.XPATH, "//div[@data-tree-id='343' and .//span[contains(text(),'Brain "
                                "stem')]]//button[3]")
    CEREBRUM_ARROW_BTN = (By.XPATH, "//div[@data-tree-id='567' and .//span[contains(text(),"
                                    "'Cerebrum')]]//button[3]")
    CEREBRAL_CORTEX_BTN = (By.XPATH, "//div[@data-tree-id='688' and .//span[contains(text(),"
                                     "'Cerebral cortex')]]//button[3]")
    CORTICAL_PLATE_BTN = (By.XPATH, "//div[@data-tree-id='695' and .//span[contains(text(),"
                                    "'Cortical plate')]]//button[3]")
    ISOCORTEX_BTN = (By.XPATH, "//div[@data-tree-id='315' and .//span[contains(text(),"
                               "'Isocortex')]]//button[3]")
    AGRANULAR_INS_AREA_BTN = (By.XPATH, "//div[@data-tree-id='95' and .//span[contains(text(),"
                                        "'Agranular insular area')]]//button[3]")
    AGRANULAR_INS_AREA_DORSAL_P_BTN = (By.XPATH, "//div[@data-tree-id='104' and .//span[contains("
                                                 "text(),'Agranular insular area, "
                                                 "dorsal part')]]//button[3]")
    AGRANULAR_INS_AREA_DORSAL_P_TITLE = (By.XPATH, "//div[@data-tree-id='104' and .//span["
                                                   "contains(text(),'Agranular insular area, "
                                                   "dorsal part')]]//button[1]")
    L5_BP_ARROW_BTN = (By.XPATH, "//div[@data-tree-id='http://uri.interlex.org/base/ilx_0383221"
                                 "?rev=34' and .//span[contains(text(), "
                                 "'L5_BP')]]/descendant::button[2]")
    L5_BP_SLIDER_HANDLE = (By.XPATH, "//div[@data-tree-id='http://uri.interlex.org/base"
                                     "/ilx_0383221?rev=34' and .//span[contains(text(), "
                                     "'L5_BP')]]//div[@class='ant-slider-rail']")
    CELL_COMP_INTERACTIVE = (By.XPATH, "//a[starts-with(@href, "
                                       "'/mmb-beta/build/cell-composition/interactive"
                                       "?brainModelConfigId=') and text()='Interactive']" )
    SECOND_SUB_MENU = (By.XPATH, "//button[@type='button' and starts-with(@class,'min-w-["
                                 "190px]')]/div[starts-with(@class,'flex flex-row')]/*[name("
                                 ")='svg']")
    TOP_NAV_MENU = (By.XPATH, "//button[@type='button' and @aria-haspopup='menu']//div[contains("
                              "text(), 'Cell composition')]")
    CELL_COMPOSITION = (By.XPATH, "//div[@role='menu']//div[contains(text(),'Cell composition')]")
    CELL_MODEL_ASSIGNMENT = (By.XPATH, "//div[@role='menu']//div[contains(text(),'Cell model "
                                       "assignment')]")
    CONNECTOME_DEFINITION = (By.XPATH, "//div[@role='menu']//div[contains(text(),'Connectome "
                                       "definition')]")
    CONNECTION_MODEL_ASSIGNMENT = (By.XPATH, "//div[@role='menu']//div[contains(text(),"
                                             "'Connection model assignment')]")
    TOP_SUB_MENU = (By.XPATH, "//button[@type='button' and starts-with(@class, 'min-w-[190px] "
                              "h-full border-l border-neutral')]/div[contains(text(), "
                              "'Interactive')]")
    SUB_MENU_CONFIGURATION = (By.XPATH, "//button[.='Configuration']")
    SUB_MENU_INTERACTIVE = (By.XPATH, "//button[text()='Interactive']")