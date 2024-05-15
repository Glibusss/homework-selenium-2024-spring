from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class RegistrationPageLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    MAIN_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'registration_panelTitle')]")
    
    MAIN_PAGE_SUBTITLE = (By.XPATH, "//*[contains(@class, 'registration_panelSubTitle')]")

    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    IMPORT_MYTARGET_CABINET_BUTTON = (By.ID, "click-exportMTButton")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")

    IMPORT_MYTARGET_CABINET_BUTTON_HINT = (By.XPATH, "//*[contains(@id, 'click-exportMTButton')]/descendant::*[contains(@class, 'Hint_hintTrigger')]")

    COUNTRY_DROPDOWN = (By.XPATH, f"//*[@data-testid='country']")

    @staticmethod
    def COUNTRY_DROPDOWN_ITEM(country_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{country_name}']"

    CURRENCY_DROPDOWN = (By.XPATH, f"//*[@data-testid='currency']")

    @staticmethod
    def CURRENCY_DROPDOWN_ITEM(currency_item):
        return By.XPATH, f"//*[@title='{currency_item}']"

    EMAIL_INPUT = (By.NAME, "email")

    INN_INPUT = (By.NAME, "inn")

    EMAIL_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::h5[text()='Email*']]"
    )

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//span[text()='{account_type}']"
    
    @staticmethod
    def ACCOUNT_TYPE_HINT(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]/descendant::*[preceding-sibling::span[text()='{account_type}']]/*[contains(@class, 'Hint_hintTrigger')]"

    @staticmethod
    def INN_ERROR(inn_name):
        return By.XPATH, f"//*[@role='alert' and preceding-sibling::h5[text()='{inn_name}']]"

    OFFER_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::div[contains(@class, 'registration_offerDesc__')]]"
    )

    SUBMIT_BUTTON = (By.XPATH, f"//*[@data-testid='create-button']")

    OFFER_CHECKBOX = (By.NAME, "offer")

    OFFER_TERMS_LINK = (By.XPATH, "//a[contains(@href, 'offer_fl')]")

    ORD_DOCS_LINK = (By.XPATH, "//a[contains(@href, 'ord_clients')]")

    TOS_LINK = (By.XPATH, "//a[contains(@href, 'adsvk/terms')]")

    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(@href, 'privacy')]")

    @staticmethod
    def MAILING_CHECKBOX(agreement_span):
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__input') and following-sibling::*[descendant::span[contains(., '{agreement_span}')]]]"

    @staticmethod
    def MAILING_CHECKBOX_HINT(agreement_span): 
        return By.XPATH, f"//*[contains(@class, 'Hint_hintTrigger') and preceding-sibling::span[contains(., '{agreement_span}')]]"