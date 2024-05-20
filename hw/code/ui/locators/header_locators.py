from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class HeaderLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']",
        )

    SELECTED_LANGUAGE = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4",
    )

    LOGO = (By.XPATH, "//*[contains(@class, 'header_logo')]")

    ACCOUNT_SWITCH = (By.XPATH, "//*[contains(@class, 'AccountSwitch_changeAccount')]")

    ACCOUNT_SWITCH_DROPDOWN = (
        By.XPATH,
        "//*[contains(@class, 'AccountSwitch_accountsDropdown')]",
    )

    ACCOUNT_LIST_ITEM = (
        By.XPATH,
        "//*[contains(@class, 'AccountSwitchListItem_account')]",
    )

    ACCOUNT_LIST_SELECTED_ITEM = (
        By.XPATH,
        "//*[contains(@class, 'AccountSwitchListItem_account') and descendant::*[contains(@class, 'vkuiIcon--check_circle_on')]]",
    )

    ALL_ACCOUNTS_LINK = (
        By.XPATH,
        "//*[contains(@class, 'AccountSwitch_allCabinetsLink')]",
    )

    BALANCE = (By.XPATH, "//*[contains(@class, 'balance_balanceWithAction')]")

    BALANCE_MODAL = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_modal')]")

    BALANCE_MODAL_CLOSE = (
        By.XPATH,
        "//*[contains(@class, 'CreateInvoiceModal_modal')]/descendant::*[contains(@class, 'vkuiModalDismissButton')]",
    )

    NOTIFICATIONS = (By.XPATH, "//*[contains(@class, 'header_bellNotifications')]")

    NOTIFICATIONS_POPUP = (
        By.XPATH,
        "//*[contains(@class, 'BellNotificationsContent_card')]",
    )

    NOTIFICATIONS_SETTINGS = (
        By.XPATH,
        "//*[contains(@class, 'BellNotificationsContent_openSettingsButton')]",
    )

    NOTIFICATIONS_SETTING_POPUP = (
        By.XPATH,
        "//*[contains(@class, 'BellNotificationsContent_settingsButton')]",
    )

    VK_ID_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_avatar')]")

    VK_ID_POPUP = (By.XPATH, "//*[contains(@class, 'userMenu_menu')]")
    