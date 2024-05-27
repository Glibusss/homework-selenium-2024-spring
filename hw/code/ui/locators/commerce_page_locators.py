from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CommercePageLocators(BasePageLocators):
    CREATE_BUTTON = (
        By.XPATH,
        "//*[@data-testid='create-catalog']",
    )

    SIDEBAR = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_')]")

    MODAL_CREATE_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_')]//*[contains(@class, 'vkuiButton__content') and text()='Создать каталог']",
    )

    NEW_CATALOG_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-2') and text()='Новый каталог']",
    )

    NAME_INPUT = (By.XPATH, "//*[@data-testid='catalogName-input']")

    @staticmethod
    def TABS_NAME(tabs):
        return (
            By.XPATH,
            f"//*[@data-testid='catalog-source_type-select']//*[text()='{tabs}']",
        )

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    CANCEL_BUTTON = (By.XPATH, "//button[@data-testid='cancel']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")

    FEED_OR_COMMUNITY_INPUT = (By.XPATH, "//input[@data-testid='catalogUrl-input']")
    PERIOD_SELECT = (By.XPATH, "//input[@data-testid='catalogPeriod-select']")

    @staticmethod
    def PERIOD_SELECT_ELEMENT(period: str):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{period}']",
        )

    SELECTED_PERIOD = (
        By.XPATH,
        "//*[following-sibling::input[@data-testid='catalogPeriod-select']]/*[contains(@class, 'vkuiText')]",
    )

    HISTORY_PERIOD = (By.XPATH, "//*[child::*[text()='Период обновления']]")

    CHECKBOX_UTM_SIGN = (
        By.XPATH,
        "//*[contains(@class, 'vkuiCheckbox')]//*[contains(@class, 'vkuiCheckbox__titleBefore') and text()='Автоматически удалять UTM-метки']",
    )

    @staticmethod
    def ALERT_SIGN(alert):
        return (By.XPATH, f"//*[text()='{alert}']")

    SELLER_INPUT = (By.XPATH, "//*[@data-testid='catalogUrl-input']")

    API_SELLER_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='API key']]//input",
    )
    MARKERPLACE_BANNER = (
        By.XPATH,
        "//*[contains(@class, 'MarketplaceTemplate_bannerWarpper__')]",
    )

    CATEGORY_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiCustomSelectInput')]")

    DOWNLOAD_BUTTON = (
        By.XPATH,
        "//*[contains(@class,'FileTemplate_button__') and @href='https://target.my.com/documents/vkads/catalog_products.csv']",
    )

    DROPZONE = (
        By.XPATH,
        "//*[contains(@class, 'FeedFileSelector_fileSelectorDescription__')]",
    )

    # Много vkuiHeadline--level-1, выбираем в хедере; таких элементов два, выбираем именно h4 с .text, а не span
    CATALOGUE_NAME_IN_SELECTOR = (
        By.XPATH,
        "//*[@data-testid='current-catalog']//*[contains(@class, 'vkuiHeadline--level-1') and following-sibling::*[contains(@class, 'Catalog')]]",
    )

    CATALOGUE_SETTINGS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton') and descendant::*[text()='Настройки']]",
    )

    SETTINGS_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-2') and text()='Настройки каталога']",
    )
