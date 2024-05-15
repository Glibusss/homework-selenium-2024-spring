from selenium.common import TimeoutException
from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from datetime import datetime


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    ERROR_TOO_LONG_AUDIENCE_NAME = 'Максимальная длина 255 символов'
    MAX_LENGTH_OF_AUDIENCE_NAME = 255

    SOURCE_TYPE_LIST = ['Существующая аудитория', 'Список пользователей', 'Ключевые фразы', 'События в рекламной кампании', 'События в мобильном приложении', 'События в лид-форме', 'События на сайте', 'Подписчики сообществ', 'Музыканты']

    def click_create_audience_button(self):
        self.click(self.locators.CREATE_AUDIENCE_BUTTON)

    def create_audience_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.CREATE_AUDIENCE_MODAL_PAGE, timeout=1)
    
    def create_audience_modal_page_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.CREATE_AUDIENCE_MODAL_PAGE, timeout=1)
    
    def audience_name_input_became_visible(self):
        return self.became_visible(self.locators.AUDIENCE_NAME_INPUT)

    def sidebar_sign_became_visible(self):
        return self.became_visible(self.locators.SIDEBAR_SIGN) and self.became_visible(self.locators.SIDEBAR_SIGN_HINTS)

    def add_source_button_became_visible(self):
        return self.became_visible(self.locators.ADD_SOURCE_BUTTON)
    
    def footer_buttons_became_visible(self):
        return self.became_visible(self.locators.CANCEL_BUTTON) and self.became_visible(self.locators.SUBMIT_BUTTON)
    
    def cross_button_became_visible(self):
        return self.became_visible(self.locators.CROSS_BUTTON)
    
    def click_cross_button(self):
        self.click(self.locators.CROSS_BUTTON, timeout=1)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON, timeout=1)

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON)

    def add_source_modal_page_became_visible(self) -> bool:
        return self.became_visible(self.locators.ADD_SOURCE_MODAL_PAGE)
    
    def source_items_became_visible(self):
        for s in self.SOURCE_TYPE_LIST:
            if not self.became_visible(self.locators.SOURCE_ITEM(s)):
                return False
        return True
    
    def key_phrases_sidebar_became_visible(self):
        return self.became_visible(self.locators.KEY_PHRASES_MODAL_PAGE)
    
    def key_phrases_textarea_became_visible(self):
        return self.became_visible(self.locators.KEY_PHRASES_INPUT)
    
    def minus_key_phrases_textarea_became_visible(self):
        return self.became_visible(self.locators.MINUS_PHRASES_INPUT)
    
    def period_input_became_visible(self):
        return self.became_visible(self.locators.PERIOD_INPUT)

    def select_source(self, source_name):
        self.click(self.locators.SOURCE_ITEM(source_name))

    def enter_key_phrases(self, key_phrases: list):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(' '.join(key_phrases))

    def click_modal_page_submit_button(self):
        try:
            self.click(self.locators.MODAL_PAGE_SUBMIT_BUTTON, timeout=5)
        except TimeoutException:
            pass

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE, timeout=10).text
    
    def delete_audience(self):
        self.hover(self.locators.CREATED_AUDIENCE_TITLE, timeout=10)
        self.hover(self.locators.MORE_BUTTON)
        self.hover(self.locators.DELETE)
        self.click(self.locators.DELETE)
        self.click(self.locators.DELETE_MODAL_BUTTON)

    def created_audience_became_invisible(self):
        return self.became_invisible(self.locators.CREATED_AUDIENCE_TITLE)
    