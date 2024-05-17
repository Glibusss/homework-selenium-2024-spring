from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

page_text = {
    'Русский': {
        'MAIN_PAGE_TITLE': 'Добро пожаловать' \
                           'в VK Рекламу',
        'MAIN_PAGE_SUBTITLE': 'Перенесите настройки и кампании из существующего рекламного кабинета или создайте новый',
        'CREATE_CABINET': 'Создать новый кабинет',
        'IMPORT_MYTARGET': 'Использовать рекламный кабинет myTarget',           
    },
    'English': {
        'MAIN_PAGE_TITLE': 'Welcome ' \
                           'to VK Ads',
        'MAIN_PAGE_SUBTITLE': 'Transfer settings and campaigns from an existing account or create a new one',
        'CREATE_CABINET': 'Create a new account',
        'IMPORT_MYTARGET': 'Use myTarget ad account',
    },
}

class RegistrationMainPageLocators(BasePageLocators):
    @staticmethod
    def TEXT(text):
        return By.XPATH, f"//*[text()='{text}']"

    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")

    MAIN_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'registration_panelTitle')]")
    
    MAIN_PAGE_SUBTITLE = (By.XPATH, "//*[contains(@class, 'registration_panelSubTitle')]")

    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    IMPORT_MYTARGET_CABINET_BUTTON = (By.ID, "click-exportMTButton")

    IMPORT_MYTARGET_CABINET_BUTTON_HINT = (By.XPATH, "//*[contains(@id, 'click-exportMTButton')]/descendant::*[contains(@class, 'Hint_hintTrigger')]")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")
