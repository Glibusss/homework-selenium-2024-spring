from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AudiencePageLocators(BasePageLocators):
    CREATE_AUDIENCE_BUTTON = (By.XPATH, "//button[@data-testid='create-audience']")
    CREATE_AUDIENCE_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Создание аудитории']]"
    )

    AUDIENCE_NAME_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiInput__el')]")

    SIDEBAR_SIGN = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Включить пользователей, которые соответствуют']")
    SIDEBAR_SIGN_HINTS = (By.XPATH, "//*[contains(@class, 'HintSelector_hintSelectorButton__') and text()='хотя бы одному из условий']")

    ERROR = (By.XPATH, "//*[@role='alert']")

    ADD_SOURCE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Добавить источник']")
    ADD_SOURCE_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Включить источник']]"
    )

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")

    @staticmethod
    def SOURCE_ITEM(item_name):
        return By.XPATH, f"//*[contains(@class, 'SourceTypeSelector_button__')]//*[text()='{item_name}']"
    
    KEY_PHRASES_MODAL_PAGE = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_') and child::h2[text()='Ключевые фразы']]"
    )

    KEY_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_textarea__')]/textarea")
    MINUS_PHRASES_INPUT = (By.XPATH, "//*[contains(@class, 'KeyPhrases_negationPhrases__')]//textarea")
    PERIOD_INPUT = (By.XPATH, "//*[contains(@class, 'Context_daysInput__')]/input")

    MODAL_PAGE_SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiTappable--hasActive') and @type='submit']")

    SOURCE_CARD_CONTENT = (
        By.XPATH,
        "//*[contains(@class, 'SourcesList_wrapper__')]//*[contains(@class, 'InfoRow_content__')]"
    )

    CREATED_AUDIENCE_TITLE = (By.XPATH, "//*[contains(@class, 'NameCell_wrapper__')]/h5")

    MORE_BUTTON = (By.XPATH, "//button[@data-testid='audience-item-menu']")

    DELETE = (By.XPATH, "//*[contains(@class, 'vkui--vkBase')]//*[text()='Удалить']")
    DELETE_MODAL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")
    