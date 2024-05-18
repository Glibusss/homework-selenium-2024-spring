from ui.pages.base_page import BasePage
from ui.locators.registration_import_mytarget_page_locators import RegistrationImportMytargetPageLocators


class RegistrationImportMytargetPage(BasePage):
    locators = RegistrationImportMytargetPageLocators()
    url = 'https://ads.vk.com/hq/registration/import/target'

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

    def back_button_became_visible(self):
        return self.became_visible(self.locators.BACK_BUTTON)
    
    def click_back_button(self):
        self.click(self.locators.BACK_BUTTON)

    def select_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(account_type))

    def account_type_switch_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_TYPE_SWITCH)

    def get_selected_account_switch(self) -> str:
        return self.find(self.locators.SWITCH_SELECTED_ACCOUNT_TYPE).get_attribute('value')
    
    def switch_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_TEXT(account_type))

    def switch_account_type_by_value(self, value: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_VALUE(value))
    
    def get_account_type_benefits(self):
        return list(zip(
            self.find_all(self.locators.IMPORT_BENEFIT_ICON),
            [item.text for item in self.find_all(self.locators.IMPORT_BENEFIT_ITEM_TITLE)],
            [item.text for item in self.find_all(self.locators.IMPORT_BENEFIT_ITEM_DESC)]
        )) 

    def import_continue_button_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_BUTTON)
    
    def click_import_continue_button(self):
        self.click(self.locators.IMPORT_CONTINUE_BUTTON)

    def import_continue_note_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_DESC)
