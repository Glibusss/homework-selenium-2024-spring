from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.commerce_page_locators import CommercePageLocators


class CommercePage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CommercePageLocators()


    TABS_LIST = ["Фид или сообщество", "Маркетплейс", "Вручную"]

    def sidebar_became_visible(self):
        return self.became_visible(self.locators.SIDEBAR)
    
    def sidebar_became_invisible(self):
        return self.became_invisible(self.locators.SIDEBAR)
    
    def new_catalog_h2_became_visible(self):
        return self.became_visible(self.locators.NEW_CATALOG_H2)
    
    def name_input_became_visible(self):
        return self.became_visible(self.locators.NAME_INPUT)
    
    def tabs_became_visible(self):
        for t in self.TABS_LIST:
            if not self.became_visible(self.locators.TABS_NAME(t)):
                return False
        return True
    
    def sidebar_buttons_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON) and self.became_visible(self.locators.CANCEL_BUTTON)
    
    def cross_button_became_visible(self):
        return self.became_visible(self.locators.CROSS_BUTTON)
    
    def feed_or_community_became_visible(self):
        return self.became_visible(self.locators.FEED_OR_COMMUNITY_INPUT) and self.became_visible(self.locators.PERIOD_SELECT) and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
    
    def input_error_feed_became_visible(self, input, error):
        feed_link = self.find(self.locators.FEED_OR_COMMUNITY_INPUT)
        feed_link.clear()
        feed_link.send_keys(input)
        self.click(self.locators.SUBMIT_BUTTON)
        return self.became_visible(self.locators.ALERT_SIGN(error))
    
    def marketplace_became_visible(self):
        return self.became_visible(self.locators.SELLER_INPUT) and self.became_visible(self.locators.MARKERPLACE_BANNER)
    
    def input_error_marketplace_became_visible(self, input, error):
        feed_link = self.find(self.locators.SELLER_INPUT)
        feed_link.clear()
        feed_link.send_keys(input)
        self.click(self.locators.SUBMIT_BUTTON)
        return self.became_visible(self.locators.ALERT_SIGN(error))
    
    def manual_became_visible(self):
        return self.became_visible(self.locators.CATEGORY_SELECT) and self.became_visible(self.locators.DOWNLOAD_BUTTON) and self.became_visible(self.locators.DROPZONE) and self.became_visible(self.locators.CHECKBOX_UTM_SIGN)
    
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
    
