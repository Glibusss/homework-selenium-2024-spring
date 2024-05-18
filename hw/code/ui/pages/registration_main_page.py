from ui.pages.base_page import BasePage
from ui.locators.registration_main_page_locators import RegistrationMainPageLocators


class RegistrationMainPage(BasePage):
    locators = RegistrationMainPageLocators()
    url = 'https://ads.vk.com/hq/registration'

    def text_became_visible(self, text: str):
        return self.became_visible(self.locators.TEXT(text))

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)
    
    def image_became_visible(self):
        return self.became_visible(self.locators.REGISTRATION_IMAGE)
    
    def click_image(self):
        self.click(self.locators.REGISTRATION_IMAGE)
    
    def language_switch_became_visible(self):
        return self.became_visible(self.locators.LANGUAGE_SWITCH)
    
    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text
    
    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))
    
    def main_page_title_became_visible(self):
        return self.became_visible(self.locators.MAIN_PAGE_TITLE)
    
    def main_page_subtitle_became_visible(self):
        return self.became_visible(self.locators.MAIN_PAGE_SUBTITLE)

    def create_new_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.CREATE_NEW_CABINET_BUTTON)
    
    def import_mytarget_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.IMPORT_MYTARGET_CABINET_BUTTON)

    def click_create_new_cabinet_button(self):
        self.click(self.locators.CREATE_NEW_CABINET_BUTTON)

    def click_import_mytarget_cabinet_button(self):
        self.click(self.locators.IMPORT_MYTARGET_CABINET_BUTTON)

    def hover_import_mytarget_cabinet_button_hint(self):
        self.hover(self.locators.IMPORT_MYTARGET_CABINET_BUTTON_HINT)

    def mytarget_hint_became_visible(self):
        return self.became_visible(self.locators.IMPORT_MYTARGET_CABINET_BUTTON_HINT)
    