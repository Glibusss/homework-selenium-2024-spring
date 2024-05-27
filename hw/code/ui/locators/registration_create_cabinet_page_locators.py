from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class RegistrationCreateCabinetPageLocators(BasePageLocators):
    @staticmethod
    def TEXT(text):
        return By.XPATH, f"//*[text()='{text}']"

    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")

    BACK_BUTTON = (By.XPATH, "//button[@data-testid='back-button']")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[text()='{language}']",
        )

    SELECTED_LANGUAGE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4",
    )

    CREATE_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'HeaderNav_headerFormTitle')]")

    # Выбираем нажимаемый элемент с радиобаттоном, у выборов типа кабинета в data-testid есть общая строка
    ACCOUNT_TYPE_BUTTON_ELEM = (
        By.XPATH,
        "//*[contains(@class, 'vkuiRadio') and contains(@class, 'vkuiTappable') and child::input[starts-with(@data-testid, 'cabinet-')]]",
    )

    # Выбираем нажимаемый элемент с радиобаттоном, у выбора типа лица в data-testid этой общей строки нет, и больше радиобаттонов на странице нет
    ENTITY_TYPE_BUTTON_ELEM = (
        By.XPATH,
        "//*[contains(@class, 'vkuiRadio') and contains(@class, 'vkuiTappable') and child::input[not(starts-with(@data-testid, 'cabinet-'))]]",
    )

    @staticmethod
    def ACCOUNT_TYPE_LABEL(label):
        return By.XPATH, f"//*[text()='{label}']"

    COUNTRY_DROPDOWN = (By.XPATH, "//*[@data-testid='country']")

    COUNTRY_DROPDOWN_LIST = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCustomSelect--pop-down') and following-sibling::*[@data-testid='country']]",
    )

    @staticmethod
    def COUNTRY_DROPDOWN_ITEM(country_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{country_name}']",
        )

    CURRENCY_DROPDOWN = (By.XPATH, "//*[@data-testid='currency']")

    CURRENCY_DROPDOWN_LIST = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCustomSelect--pop-down') and following-sibling::*[@data-testid='currency']]",
    )

    @staticmethod
    def CURRENCY_DROPDOWN_ITEM(currency_item):
        return By.XPATH, f"//*[@title='{currency_item}']"

    EMAIL_INPUT = (By.NAME, "email")

    INN_INPUT = (By.NAME, "inn")

    NAME_INPUT = (By.NAME, "name")

    EMAIL_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::*[text()='Email*']]",
    )

    ROW_INDIVIDUAL_WARNING = (By.XPATH, "//*[contains(@class, 'Warning_container')]")

    ROW_INDIVIDUAL_WARNING_TEXT = (By.XPATH, "//*[contains(@class, 'Warning_inner')]")

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiRadio__title')]//*[text()='{account_type}']",
        )

    # Есть ещё один Hint_hintTrigger вне выбора типа аккаунта
    @staticmethod
    def ACCOUNT_TYPE_HINT(account_type):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiRadio__title')]/descendant::*[preceding-sibling::*[text()='{account_type}']]/*[contains(@class, 'Hint_hintTrigger')]",
        )

    # Существует другой Tooltip_tooltipContainer (у чекбокса согласия на рассылку)
    ACCOUNT_TYPE_HINT_WINDOW = (
        By.XPATH,
        "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]",
    )

    ACCOUNT_TYPE_HINT_WINDOW_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]/descendant::*[contains(@class, 'UserView_title')]",
    )

    ACCOUNT_TYPE_HINT_WINDOW_TEXT = (
        By.XPATH,
        "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]/descendant::*[contains(@class, 'UserView_description')]",
    )

    @staticmethod
    def INN_ERROR(inn_label):
        return (
            By.XPATH,
            f"//*[@role='alert' and preceding-sibling::*[text()='{inn_label}']]",
        )

    OFFER_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::*[contains(@class, 'registration_offerDesc__')]]",
    )

    SUBMIT_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")

    OFFER_CHECKBOX = (By.NAME, "offer")

    @staticmethod
    def CHECKBOX_IS_CHECKED_OR_NOT(checkbox, state):
        return (
            By.XPATH,
            f"//label[contains(@class, 'vkuiCheckbox') and .//*[text()='{checkbox}']]//*[contains(@class, 'vkuiCheckbox__icon--{state}')]",
        )

    OFFER_TERMS_LINK = (By.XPATH, "//a[contains(@href, 'documents/offer')]")

    ORD_DOCS_LINK = (By.XPATH, "//a[contains(@href, 'ord_clients')]")

    TOS_LINK = (By.XPATH, "//a[contains(@href, 'adsvk/terms')]")

    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(@href, 'privacy')]")

    @staticmethod
    def MAILING_CHECKBOX(checkbox_label):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCheckbox__icon') and following-sibling::*[descendant::*[contains(., '{checkbox_label}')]]]",
        )

    @staticmethod
    def MAILING_CHECKBOX_HINT(checkbox_label):
        return (
            By.XPATH,
            f"//*[contains(@class, 'Hint_hintTrigger') and preceding-sibling::*[contains(., '{checkbox_label}')]]",
        )

    CREATE_CABINET_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")

    MAILING_CHECKBOX_HINT_WINDOW = (
        By.XPATH,
        "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'registration_hint_')]",
    )
