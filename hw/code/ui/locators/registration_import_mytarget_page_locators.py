from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class RegistrationImportMytargetPageLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")

    BACK_BUTTON = (By.XPATH, "//button[@data-testid='back-button']")

    @staticmethod
    def TEXT(text):
        return By.XPATH, f"//*[text()='{text}']"

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")

    ACCOUNT_TYPE_SWITCH = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControl__in')]")

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//*[text()='{account_type}']"

    @staticmethod
    def ACCOUNT_TYPE_SELECTOR_BY_TEXT(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[following-sibling::*[text()='{account_type}']]"
    
    @staticmethod
    def ACCOUNT_TYPE_SELECTOR_BY_VALUE(value):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[@value='{value}']"
    
    SWITCH_SELECTED_ACCOUNT_TYPE = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControlOption--checked')]/descendant::input")

    SWITCH_SELECTED_ACCOUNT_LABEL = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControlOption--checked')]/descendant::h4")

    IMPORT_BENEFIT_ITEM = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCell_')]")

    IMPORT_BENEFIT_ICON = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCell')]/descendant::*[contains(@class, 'vkuiIcon')]")

    IMPORT_BENEFIT_ITEM_TITLE = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCellTitle')]")

    IMPORT_BENEFIT_ITEM_DESC = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCellDesc')]")

    IMPORT_CONTINUE_BUTTON = (By.XPATH, "//*[@data-testid='import-continue']")

    IMPORT_CONTINUE_DESC = (By.XPATH, "//*[contains(@class, 'ImportPanel_actionDesc')]")
    
