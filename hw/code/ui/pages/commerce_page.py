from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.commerce_page_locators import CommercePageLocators


class CommercePage(BasePage):
    url = "https://ads.vk.com/hq/ecomm/catalogs"
    locators = CommercePageLocators()

    TABS_LIST = ["Фид или сообщество", "Маркетплейс", "Вручную"]

    ERRORS_FEED_LIST = [
        "Необходимо указать протокол http(s)",
        "Невалидный url",
        "Неверный формат файла",
        "Не удалось выполнить запрос по HTTP",
    ]
    INPUTS_FEED_LIST = [
        "h",
        "http://",
        "https://nota-tabula.ru",
        "https://nota-tabula.rur",
    ]

    ERRORS_MARKETPLACE_LIST = [
        "Необходимо указать протокол http(s)",
        "Невалидный url",
        "Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе",
    ]
    INPUTS_MARKETPLACE_LIST = [
        "h",
        "http://",
        "https://www.wildberries.rus/brands/310451382-miryuyu",
    ]

    def sidebar_became_visible(self):
        return self.became_visible(self.locators.SIDEBAR)

    def sidebar_became_invisible(self):
        return self.became_invisible(self.locators.SIDEBAR)

    def new_catalog_has_h2_content_title(self):
        return self.became_visible(self.locators.NEW_CATALOG_H2)

    def name_input_became_visible(self):
        return self.became_visible(self.locators.NAME_INPUT)

    def has_tabs_content(self):
        for t in self.TABS_LIST:
            if not self.became_visible(self.locators.TABS_NAME(t)):
                return False
        return True

    def sidebar_buttons_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON) and self.became_visible(
            self.locators.CANCEL_BUTTON
        )

    def cross_button_became_visible(self):
        return self.became_visible(self.locators.CROSS_BUTTON)

    def has_feed_or_community_tabs_content(self):
        return (
            self.became_visible(self.locators.FEED_OR_COMMUNITY_INPUT)
            and self.became_visible(self.locators.PERIOD_SELECT)
            and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
        )

    def has_input_error_feed_content(self):
        for i in range(0, 4):
            feed_link = self.find(self.locators.SELLER_INPUT)
            feed_link.clear()
            feed_link.send_keys(self.INPUTS_FEED_LIST[i])
            self.click(self.locators.SUBMIT_BUTTON)
            if not self.became_visible(
                self.locators.ALERT_SIGN(self.ERRORS_FEED_LIST[i])
            ):
                return False
        return True

    def has_marketplace_tabs_content(self):
        return self.became_visible(self.locators.SELLER_INPUT) and self.became_visible(
            self.locators.MARKERPLACE_BANNER
        )

    def has_input_error_marketplace_content(self, input, error):
        for i in range(0, 3):
            feed_link = self.find(self.locators.SELLER_INPUT)
            feed_link.clear()
            feed_link.send_keys(self.INPUTS_MARKETPLACE_LIST[i])
            self.click(self.locators.SUBMIT_BUTTON)
            self.became_visible(self.locators.ALERT_SIGN(self.ERRORS_MARKETPLACE_LIST))

    def has_manual_tabs_content(self):
        return (
            self.became_visible(self.locators.CATEGORY_SELECT)
            and self.became_visible(self.locators.DOWNLOAD_BUTTON)
            and self.became_visible(self.locators.DROPZONE)
            and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
        )

    def click_create_button(self):
        self.click(self.locators.CREATE_BUTTON)

    def click_feed_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[0]))

    def click_marketplace_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[1]))

    def click_manual_tabs(self):
        self.click(self.locators.TABS_NAME(self.TABS_LIST[2]))

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

    def click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON)

