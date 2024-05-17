from ui.pages.base_page import BasePage
from ui.locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
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
    
    def click_back_button(self):
        self.click(self.locators.BACK_BUTTON)
    
    def create_page_title_became_visible(self):
        return self.became_visible(self.locators.CREATE_PAGE_TITLE)

    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text
    
    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))

    def account_type_label_became_visible(self, language: str):
        return len(self.find_multiple(self.locators.ACCOUNT_TYPE_LABEL(language))) == 2
    
    def account_type_buttons_became_visible(self):
        return len(self.find_multiple(self.locators.ACCOUNT_TYPE_BUTTON_ELEM)) == 2
    
    def entity_type_buttons_became_visible(self):
        return len(self.find_multiple(self.locators.ENTITY_TYPE_BUTTON_ELEM)) == 2
    
    def entity_type_button_count(self):
        return len(self.find_multiple(self.locators.ENTITY_TYPE_BUTTON_ELEM))
    
    def row_individual_warning_became_visible(self):
        return self.became_visible(self.locators.ROW_INDIVIDUAL_WARNING)
    
    def hover_account_type_hint(self, account_type: str):
        self.hover(self.locators.ACCOUNT_TYPE_HINT(account_type))

    def account_type_hint_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_TYPE_HINT_WINDOW)
    
    def get_account_type_hint(self):
        return (
            self.find(self.locators.ACCOUNT_TYPE_HINT_WINDOW_TITLE).text,
            self.find(self.locators.ACCOUNT_TYPE_HINT_WINDOW_TEXT).text,
        )

    def country_selector_became_visible(self):
        return self.became_visible(self.locators.COUNTRY_DROPDOWN)

    def click_country_selector(self):
        self.click(self.locators.COUNTRY_DROPDOWN)

    def country_list_became_visible(self):
        return self.became_visible(self.locators.COUNTRY_DROPDOWN_LIST)

    def select_country(self, country_name: str):
        self.click(self.locators.COUNTRY_DROPDOWN)
        self.click(self.locators.COUNTRY_DROPDOWN_ITEM(country_name))

    def currency_selector_became_visible(self):
        return self.became_visible(self.locators.CURRENCY_DROPDOWN)

    def click_currency_selector(self):
        self.click(self.locators.CURRENCY_DROPDOWN)

    def currency_list_became_visible(self):
        return self.became_visible(self.locators.CURRENCY_DROPDOWN_LIST)

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

    def get_inn_error(self, language: str, timeout: int=None) -> str:
        return self.find(self.locators.INN_ERROR(language), timeout).text

    def get_offer_error(self) -> str:
        return self.find(self.locators.OFFER_ERROR).text
    
    def offer_checkbox_became_visible(self):
        return self.became_invisible(self.locators.OFFER_CHECKBOX)

    def click_offer_checkbox(self):
        self.scroll_and_click(self.locators.OFFER_CHECKBOX)

    def mailing_checkbox_became_visible(self, language: str):
        return self.became_visible(self.locators.MAILING_CHECKBOX(language))
    
    def click_mailing_checkbox(self, language: str):
        self.scroll_and_click(self.locators.MAILING_CHECKBOX(language))

    def checkbox_checked(self, label: str):
        return self.became_visible(self.locators.CHECKBOX_IS_CHECKED_OR_NOT(label, 'on'))
    
    def checkbox_unchecked(self, label: str):
        return self.became_visible(self.locators.CHECKBOX_IS_CHECKED_OR_NOT(label, 'off'))

    def email_input_became_visible(self):
        return self.became_visible(self.locators.EMAIL_INPUT)

    def enter_email(self, email: str):
        elem = self.find(self.locators.EMAIL_INPUT)
        elem.clear()
        elem.send_keys(email)

    def inn_input_became_visible(self):
        return self.became_visible(self.locators.INN_INPUT)

    def enter_inn(self, inn: str):
        elem = self.find(self.locators.INN_INPUT)
        elem.clear()
        elem.send_keys(inn)

    def get_entered_inn(self):
        return self.find(self.locators.INN_INPUT).get_attribute('value')

    def name_input_became_visible(self):
        return self.became_visible(self.locators.NAME_INPUT)
    
    def enter_name(self, name: str):
        elem = self.find(self.locators.NAME_INPUT)
        elem.clear()
        elem.send_keys(name)

    def offer_link_became_visible(self):
        return self.became_visible(self.locators.OFFER_TERMS_LINK)

    def click_offer_link(self):
        self.click(self.locators.OFFER_TERMS_LINK)
        self.go_to_new_tab()

    def ord_link_became_visible(self):
        return self.became_visible(self.locators.ORD_DOCS_LINK)

    def click_ord_link(self):
        self.click(self.locators.ORD_DOCS_LINK)
        self.go_to_new_tab()

    def tos_link_became_visible(self):
        return self.became_visible(self.locators.TOS_LINK)

    def click_tos_link(self):
        self.click(self.locators.TOS_LINK)
        self.go_to_new_tab()

    def privacy_policy_link_became_visible(self):
        return self.became_visible(self.locators.PRIVACY_POLICY_LINK)

    def click_privacy_policy_link(self):
        self.click(self.locators.PRIVACY_POLICY_LINK)
        self.go_to_new_tab()

    def mailing_checkbox_became_visible(self, language: str):
        return self.became_visible(self.locators.MAILING_CHECKBOX(language))
    
    def mailing_hint_became_visible(self, language: str):
        return self.became_visible(self.locators.MAILING_CHECKBOX_HINT(language))

    def hover_mailing_hint(self, language: str):
        self.hover(self.locators.MAILING_CHECKBOX_HINT(language))

    def mailing_hint_window_became_visible(self):
        return self.became_visible(self.locators.MAILING_CHECKBOX_HINT_WINDOW)

    def create_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.CREATE_CABINET_BUTTON)
    
    def click_create_cabinet_button(self):
        self.scroll_and_click(self.locators.CREATE_CABINET_BUTTON)

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