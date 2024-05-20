from ui.pages.base_page import BasePage
from ui.locators.registration_create_cabinet_page_locators import RegistrationCreateCabinetPageLocators


class RegistrationCreateCabinetPage(BasePage):
    locators = RegistrationCreateCabinetPageLocators()
    url = 'https://ads.vk.com/hq/registration/new'

    page_text = {
        'Русский': {
            'BACK_BUTTON': 'Назад',
            'CREATE_PAGE_TITLE': 'Регистрация кабинета',
            'ACCOUNT_TYPE': 'Тип аккаунта',
            'ADVERTISER_NOMINATIVE': 'Рекламодатель',
            'AGENCY_NOMINATIVE': 'Агентство',
            'CHOOSE_COUNTRY': 'Выберите страну',
            'RUSSIA': 'Россия',
            'ARMENIA': 'Армения',
            'CURRENCY': 'Валюта',
            'RUBLE': 'Российский рубль (RUB)',
            'DOLLAR': 'Доллар США (USD)',
            'EURO': 'Евро (EUR)',
            'FIELD_REQUIRED': 'Обязательное поле',
            'EMAIL_INCORRECT': 'Некорректный email адрес',
            'INDIVIDUAL': 'Физическое лицо',
            'INDIVIDUAL_HINT': 'Не требуется заключение договора. Доступные методы оплаты - банковская карта, электронные деньги, платеж со счета телефона.',
            'ROW_INDIVIDUAL_WARNING': 'Создание рекламного кабинета для физических лиц доступно только при выборе России.',
            'LEGAL_ENTITY': 'Юридическое лицо',
            'LEGAL_ENTITY_HINT': 'Потребуется предоставить реквизиты юридического лица. В конце каждого месяца клиенту предоставляется бухгалтерская отчётность. Доступные методы оплаты - банковский перевод для юридических лиц.',
            'INN': 'ИНН',
            'INN_EXAMPLE': 'Пример: 100303539843',
            'INN_SHORT': 'Минимальная длина 12',
            'INN_LONG': 'Максимальная длина 12 символов',
            'FULL_NAME': 'ФИО',
            'ACCEPT_CHECKBOX': 'Создавая кабинет, вы принимаете условия',
            'OFFER': 'Оферты',
            'ORD': 'Соглашение о передаче рекламных данных',
            'TOS': 'Правила пользования сервисом',
            'PRIVACY': 'Политику конфиденциальности',
            'MAILING': 'Даю согласие на получение рассылок информационного и рекламно-информационного содержания',
            'MAILING_HINT': 'Соглашение регулирует получение уведомлений следующего характера:\n\n'
                            '– сообщения ВКонтакте\n'
                            '– уведомления в разделе «Колокольчик» ВКонтакте\n'
                            '– email-рассылки\n'
                            '– push-уведомления\n'
                            '– звонки\n'
                            '– смс-сообщения',
        },
        'English': {
            'BACK_BUTTON': 'Back',
            'CREATE_PAGE_TITLE': 'Account registration',
            'ACCOUNT_TYPE': 'Account type',
            'ADVERTISER_NOMINATIVE': 'Advertiser',
            'AGENCY_NOMINATIVE': 'Agency',
            'CHOOSE_COUNTRY': 'Choose a country',
            'RUSSIA': 'Russian Federation',
            'ARMENIA': 'Armenia',
            'CURRENCY': 'Currency',
            'RUBLE': 'Russian ruble (RUB)',
            'DOLLAR': 'U.S. dollar (USD)',
            'EURO': 'Euro (EUR)',
            'FIELD_REQUIRED': 'Required field',
            'EMAIL_INCORRECT': 'Invalid email address',
            'INDIVIDUAL': 'Individual',
            'INDIVIDUAL_HINT': 'You can easily open an individual account by accepting the T&Cs online.\n\n'
                               'Available payment methods: credit card, payment systems such as PayPal, etc.\n\n'
                               'Note: the account type cannot be changed after the account has been created.',
            'ROW_INDIVIDUAL_WARNING': 'Creating an advertising account for individuals is available only when choosing Russia.',
            'LEGAL_ENTITY': 'Legal entity',
            'LEGAL_ENTITY_HINT': 'This account type is mostly used for businesses with a legal entity. \n\n'
                                 'Available payment methods: credit card, payment systems such as PayPal, etc.\n\n'
                                 'Note: the account type cannot be changed once the account has been created.',
            'INN': 'TIN',
            'INN_EXAMPLE': 'Example: 100303539843',
            'INN_SHORT': 'Min length 12',
            'INN_LONG': 'Maximum length of 12 characters',
            'FULL_NAME': 'Full name',
            'ACCEPT_CHECKBOX': 'By creating an account you accept the terms',
            'OFFER': 'Offer',
            'ORD': 'Advertising data transfer agreement',
            'TOS': 'Terms of use of the service',
            'PRIVACY': 'Privacy Policy',
            'MAILING': 'I agree to receive information and promotional newsletters',
            'MAILING_HINT': 'The agreement regulates the receipt of notifications such as:\n\n'
                            '– VK messages\n'
                            '– notifications in the "Bell" section of VK\n'
                            '– email notifications\n'
                            '– push notifications\n'
                            '– calls\n'
                            '– sms-messages',
        },
    }

    ADVERTISER_ENTITY_TYPE_COUNT = 2
    AGENCY_ENTITY_TYPE_COUNT = 1

    def language_options_became_visible(self) -> bool:
        return (
            self.became_visible(self.locators.TEXT('Русский')) &
            self.became_visible(self.locators.TEXT('English'))
        )

    def language_text_became_visible(self, language: str) -> bool:
        return (
            self.became_visible(self.locators.TEXT(self.page_text[language]['BACK_BUTTON'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['CREATE_PAGE_TITLE'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['ACCOUNT_TYPE'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['ADVERTISER_NOMINATIVE'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['AGENCY_NOMINATIVE'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['CHOOSE_COUNTRY'])) &
            self.country_list_contains_russia_and_other(language) & 
            self.became_visible(self.locators.TEXT(self.page_text[language]['CURRENCY'])) &
            self.check_russia_currency_options(language) &
            self.check_row_currency_options(language) &
            self.check_row_individual_warning(language) &
            self.check_individual_hint_content(language) &
            self.check_legal_entity_hint_content(language) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['INN'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['FULL_NAME'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['ACCEPT_CHECKBOX'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['OFFER'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['ORD'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['TOS'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['PRIVACY'])) &
            self.became_visible(self.locators.TEXT(self.page_text[language]['MAILING'])) &
            self.check_mailing_hint_content(language)
        )

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)
    
    def image_became_visible(self):
        return self.became_visible(self.locators.REGISTRATION_IMAGE)
    
    def click_image(self):
        self.click(self.locators.REGISTRATION_IMAGE)

    def hover_image(self):
        self.hover(self.locators.REGISTRATION_IMAGE)
    
    def language_switch_became_visible(self):
        return self.became_visible(self.locators.LANGUAGE_SWITCH)

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
        return len(self.find_all(self.locators.ACCOUNT_TYPE_LABEL(self.page_text[language]['ACCOUNT_TYPE']))) == 2
    
    def account_type_buttons_became_visible(self):
        return len(self.find_all(self.locators.ACCOUNT_TYPE_BUTTON_ELEM)) == 2
    
    def entity_type_buttons_became_visible(self):
        return len(self.find_all(self.locators.ENTITY_TYPE_BUTTON_ELEM)) == 2
    
    def entity_type_button_count(self):
        return len(self.find_all(self.locators.ENTITY_TYPE_BUTTON_ELEM))
    
    def select_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(account_type))

    def select_individual_account(self, language: str): 
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(self.page_text[language]['INDIVIDUAL']))

    def select_legal_entity_account(self, language: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(self.page_text[language]['LEGAL_ENTITY']))

    def select_advertiser_account(self, language: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(self.page_text[language]['ADVERTISER_NOMINATIVE']))

    def select_agency_account(self, language: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(self.page_text[language]['AGENCY_NOMINATIVE']))
    
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
    
    def check_individual_hint_content(self, language: str):
        self.hover_account_type_hint(self.page_text[language]['INDIVIDUAL'])
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['INDIVIDUAL_HINT']))
        self.hover_image()
        return check
    
    def check_legal_entity_hint_content(self, language: str):
        self.hover_account_type_hint(self.page_text[language]['LEGAL_ENTITY'])
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['LEGAL_ENTITY_HINT']))
        self.hover_image()
        return check

    def country_selector_became_visible(self):
        return self.became_visible(self.locators.COUNTRY_DROPDOWN)

    def click_country_selector(self):
        self.click(self.locators.COUNTRY_DROPDOWN)

    def country_list_became_visible(self):
        return self.became_visible(self.locators.COUNTRY_DROPDOWN_LIST)
    
    def country_list_contains_russia_and_other(self, language: str) -> bool:
        self.click_country_selector()
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['RUSSIA'])) & \
                self.became_visible(self.locators.TEXT(self.page_text[language]['ARMENIA']))
        self.click_image()
        return check

    def select_country(self, country_name: str):
        self.click(self.locators.COUNTRY_DROPDOWN)
        self.click(self.locators.COUNTRY_DROPDOWN_ITEM(country_name))

    def select_russia(self, language: str):
        self.select_country(self.page_text[language]['RUSSIA'])

    def select_row_country(self, language: str):
        self.select_country(self.page_text[language]['ARMENIA'])

    def check_row_individual_warning(self, language: str):
        self.select_country(self.page_text[language]['ARMENIA'])
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['ROW_INDIVIDUAL_WARNING']))
        self.select_country(self.page_text[language]['RUSSIA'])
        return check

    def currency_selector_became_visible(self):
        return self.became_visible(self.locators.CURRENCY_DROPDOWN)

    def click_currency_selector(self):
        self.click(self.locators.CURRENCY_DROPDOWN)

    def currency_list_became_visible(self):
        return self.became_visible(self.locators.CURRENCY_DROPDOWN_LIST)
    
    def check_russia_currency_options(self, language: str):
        self.click_currency_selector()
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['RUBLE']))
        self.click_image()
        return check
    
    def check_row_currency_options(self, language: str):
        self.select_country(self.page_text[language]['ARMENIA'])
        self.click_currency_selector()
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['DOLLAR'])) & \
                self.became_visible(self.locators.TEXT(self.page_text[language]['EURO']))
        self.click_image()
        return check

    def currency_dropdown_contain_items(self, item_names: list):
        self.click(self.locators.CURRENCY_DROPDOWN)
        for item_name in item_names:
            item = self.find(self.locators.CURRENCY_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

            return True

    def click_submit_button(self):
        self.scroll_and_click(self.locators.SUBMIT_BUTTON)

    def get_email_error(self, timeout: int=None) -> str:
        return self.find(self.locators.EMAIL_ERROR, timeout).text

    def get_inn_error(self, language: str, timeout: int=None) -> str:
        return self.find(self.locators.INN_ERROR(self.page_text[language]['INN']), timeout).text

    def get_offer_error(self) -> str:
        return self.find(self.locators.OFFER_ERROR).text
    
    def offer_checkbox_became_visible(self):
        return self.became_invisible(self.locators.OFFER_CHECKBOX)

    def click_offer_checkbox(self):
        self.scroll_and_click(self.locators.OFFER_CHECKBOX)
  
    def checkbox_checked(self, label: str):
        return self.became_visible(self.locators.CHECKBOX_IS_CHECKED_OR_NOT(label, 'on'))
    
    def checkbox_unchecked(self, label: str):
        return self.became_visible(self.locators.CHECKBOX_IS_CHECKED_OR_NOT(label, 'off'))
    
    def offer_checkbox_checked(self, language: str):
        return self.checkbox_checked(self.page_text[language]['ACCEPT_CHECKBOX'])
    
    def offer_checkbox_unchecked(self, language: str):
        return self.checkbox_unchecked(self.page_text[language]['ACCEPT_CHECKBOX'])
    
    def mailing_checkbox_checked(self, language: str):
        return self.checkbox_checked(self.page_text[language]['MAILING'])
    
    def mailing_checkbox_unchecked(self, language: str):
        return self.checkbox_unchecked(self.page_text[language]['MAILING'])

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
        return self.became_visible(self.locators.MAILING_CHECKBOX(self.page_text[language]['MAILING']))
    
    def click_mailing_checkbox(self, language: str):
        self.scroll_and_click(self.locators.MAILING_CHECKBOX(self.page_text[language]['MAILING']))
    
    def mailing_hint_became_visible(self, language: str):
        return self.became_visible(self.locators.MAILING_CHECKBOX_HINT(self.page_text[language]['MAILING']))

    def hover_mailing_hint(self, language: str):
        self.hover(self.locators.MAILING_CHECKBOX_HINT(self.page_text[language]['MAILING']))

    def mailing_hint_window_became_visible(self):
        return self.became_visible(self.locators.MAILING_CHECKBOX_HINT_WINDOW)
    
    def check_mailing_hint_content(self, language: str):
        self.hover_mailing_hint(language)
        check = self.became_visible(self.locators.TEXT(self.page_text[language]['MAILING_HINT']))
        self.hover_image()
        return check

    def create_cabinet_button_became_visible(self):
        return self.became_visible(self.locators.CREATE_CABINET_BUTTON)
    
    def click_create_cabinet_button(self):
        self.scroll_and_click(self.locators.CREATE_CABINET_BUTTON)
        