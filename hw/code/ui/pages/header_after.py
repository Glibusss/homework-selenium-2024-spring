from ui.pages.base_page import BasePage
from ui.locators.header_locators import HeaderLocators


# url различается, т. к. домашняя страница у аккаунта с кабинетом и набор кнопок в хедере разные
class HeaderAfter(BasePage):
    locators = HeaderLocators()
    url = "https://ads.vk.com/hq/overview"

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)

    def click_header(self):
        self.click(self.locators.HEADER)

    def logo_became_visible(self):
        return self.became_visible(self.locators.LOGO)

    def click_logo(self):
        self.click(self.locators.LOGO)

    def account_selector_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_SWITCH)

    def click_account_selector(self):
        self.click(self.locators.ACCOUNT_SWITCH)

    def account_selector_dropdown_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_SWITCH_DROPDOWN)

    def account_selector_dropdown_became_invisible(self):
        return self.became_invisible(self.locators.ACCOUNT_SWITCH_DROPDOWN)

    def get_account_selector_accounts(self):
        return self.find_all(self.locators.ACCOUNT_LIST_ITEM)

    def get_account_selector_selected_account(self):
        # Позволит при необходимости проверить, что таких больше одного
        return self.find_all(self.locators.ACCOUNT_LIST_SELECTED_ITEM)

    def all_accounts_link_became_visible(self):
        return self.became_visible(self.locators.ALL_ACCOUNTS_LINK)

    def click_all_accounts_link(self):
        self.click(self.locators.ALL_ACCOUNTS_LINK)

    def balance_became_visible(self):
        return self.became_visible(self.locators.BALANCE)

    def click_balance(self):
        self.click(self.locators.BALANCE)

    def balance_modal_became_visible(self):
        return self.became_visible(self.locators.BALANCE_MODAL)

    def balance_modal_close_became_visible(self):
        return self.became_visible(self.locators.BALANCE_MODAL_CLOSE)

    def click_balance_modal_close(self):
        self.click(self.locators.BALANCE_MODAL_CLOSE)

    def balance_modal_became_invisible(self):
        return self.became_invisible(self.locators.BALANCE_MODAL)

    def notifications_became_visible(self):
        return self.became_visible(self.locators.NOTIFICATIONS)

    def click_notifications(self):
        self.click(self.locators.NOTIFICATIONS)

    def notifications_popup_became_visible(self):
        return self.became_visible(self.locators.NOTIFICATIONS_POPUP)

    def notifications_popup_became_invisible(self):
        return self.became_invisible(self.locators.NOTIFICATIONS_POPUP)

    def notifications_settings_became_visible(self):
        return self.became_visible(self.locators.NOTIFICATIONS_SETTINGS)

    def notifications_settings_became_invisible(self):
        return self.became_invisible(self.locators.NOTIFICATIONS_SETTINGS)

    def click_notification_settings(self):
        self.click(self.locators.NOTIFICATIONS_SETTINGS)

    def notifications_settings_popup_became_visible(self):
        return self.became_visible(self.locators.NOTIFICATIONS_SETTING_POPUP)

    def vk_id_became_visible(self):
        return self.became_visible(self.locators.VK_ID_BUTTON)

    def click_vk_id(self):
        self.click(self.locators.VK_ID_BUTTON)

    def vk_id_popup_became_visible(self):
        return self.became_visible(self.locators.VK_ID_POPUP)
    