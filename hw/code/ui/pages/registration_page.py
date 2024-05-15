from ui.pages.base_page import BasePage
from ui.locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
    url = 'https://ads.vk.com/hq/registration'

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)
    
    def language_switch_became_visible(self):
        return self.became_visible(self.locators.LANGUAGE_SWITCH)
    
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
        return self.became_visible(self.locators.IMPORT_MYTARGET_CABINET_HINT)
    
    def back_button_became_visible(self):
        return self.became_visible(self.locators.BACK_BUTTON)
    
    def create_page_title_became_visible(self, language: str):
        return self.became_visible(self.locators.CREATE_PAGE_TITLE)

    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text

    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))

    def account_type_label_became_visible(self, language: str):
        return self.find_multiple(self.locators.ACCOUNT_TYPE_LABEL(language))

    def select_country(self, country_name: str):
        self.click(self.locators.COUNTRY_DROPDOWN)
        self.click(self.locators.COUNTRY_DROPDOWN_ITEM(country_name))

    def currency_dropdown_contain_items(self, item_names: list):
        self.click(self.locators.CURRENCY_DROPDOWN)
        for item_name in item_names:
            item = self.find(self.locators.CURRENCY_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

            return True

    def click_submit_button(self):
        self.scroll_and_click(self.locators.SUBMIT_BUTTON)

    def get_email_error(self) -> str:
        return self.find(self.locators.EMAIL_ERROR).text

    def get_inn_error(self) -> str:
        return self.find(self.locators.INN_ERROR).text

    def get_offer_error(self) -> str:
        return self.find(self.locators.OFFER_ERROR).text

    def click_offer_checkbox(self):
        self.scroll_and_click(self.locators.OFFER_CHECKBOX)

    def enter_email(self, email: str):
        elem = self.find(self.locators.EMAIL_INPUT)
        elem.clear()
        elem.send_keys(email)

    def enter_inn(self, inn: str):
        elem = self.find(self.locators.INN_INPUT)
        elem.clear()
        elem.send_keys(inn)

    def select_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(account_type))

    def account_type_switch_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_TYPE_SWITCH)

    def get_selected_account_switch(self) -> str:
        return self.find(self.locators.SELECTED_ACCOUNT_TYPE).get_attribute('value')
    
    def switch_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_TEXT(account_type))

    def switch_account_type_by_value(self, value: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_VALUE(value))
    
    def get_account_type_benefits(self):
        return list(zip(
            self.find_multiple(self.locators.IMPORT_BENEFIT_ICON),
            [item.text for item in self.find_multiple(self.locators.IMPORT_BENEFIT_ITEM_TITLE)],
            [item.text for item in self.find_multiple(self.locators.IMPORT_BENEFIT_ITEM_DESC)]
        )) 

    def import_continue_button_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_BUTTON)
    
    def click_import_continue_button(self):
        self.click(self.locators.IMPORT_CONTINUE_BUTTON)

    def import_continue_note_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_DESC)

    def physical_type_became_invisible(self) -> bool:
        return self.became_invisible(self.locators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))

    def physical_type_became_visible(self) -> bool:
        return self.became_visible(self.locators.ACCOUNT_TYPE_BUTTON('Физическое лицо'))