from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

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
        'LEGAL_ENTITY_HINT': 'This account type is mostly used for businesses with a legal entity.\n\n' 
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

class RegistrationCreateCabinetPageLocators(BasePageLocators):
    @staticmethod
    def TEXT(text):
        return By.XPATH, f"//*[text()='{text}']"

    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")    

    BACK_BUTTON = (By.XPATH, "//button[@data-testid='back-button']")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")

    CREATE_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'HeaderNav_headerFormTitle')]")

    # Выбираем нажимаемый элемент с радиобаттоном, у выборов типа кабинета в data-testid есть общая строка
    ACCOUNT_TYPE_BUTTON_ELEM = (By.XPATH, "//*[contains(@class, 'vkuiRadio') and contains(@class, 'vkuiTappable') and child::input[starts-with(@data-testid, 'cabinet-')]]")

    # Выбираем нажимаемый элемент с радиобаттоном, у выбора типа лица в data-testid этой общей строки нет, и больше радиобаттонов на странице нет
    ENTITY_TYPE_BUTTON_ELEM = (By.XPATH, "//*[contains(@class, 'vkuiRadio') and contains(@class, 'vkuiTappable') and child::input[not(starts-with(@data-testid, 'cabinet-'))]]")

    @staticmethod
    def ACCOUNT_TYPE_LABEL(language):
        return By.XPATH, f"//*[text()='{page_text[language]['ACCOUNT_TYPE']}']"
    
    COUNTRY_DROPDOWN = (By.XPATH, f"//*[@data-testid='country']")

    COUNTRY_DROPDOWN_LIST = (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelect--pop-down') and following-sibling::*[@data-testid='country']]")

    @staticmethod
    def COUNTRY_DROPDOWN_ITEM(country_name):
        return By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption') and text()='{country_name}']"

    CURRENCY_DROPDOWN = (By.XPATH, f"//*[@data-testid='currency']")

    CURRENCY_DROPDOWN_LIST = (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelect--pop-down') and following-sibling::*[@data-testid='currency']]")

    @staticmethod
    def CURRENCY_DROPDOWN_ITEM(currency_item):
        return By.XPATH, f"//*[@title='{currency_item}']"

    EMAIL_INPUT = (By.NAME, "email")

    INN_INPUT = (By.NAME, "inn")

    NAME_INPUT = (By.NAME, "name")

    EMAIL_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::*[text()='Email*']]"
    )

    ROW_INDIVIDUAL_WARNING = (By.XPATH, "//*[contains(@class, 'Warning_container')]")

    ROW_INDIVIDUAL_WARNING_TEXT = (By.XPATH, "//*[contains(@class, 'Warning_inner')]")

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//*[text()='{account_type}']"

    # Есть ещё один Hint_hintTrigger вне выбора типа аккаунта    
    @staticmethod
    def ACCOUNT_TYPE_HINT(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]/descendant::*[preceding-sibling::*[text()='{account_type}']]/*[contains(@class, 'Hint_hintTrigger')]"
    
    # Существует другой Tooltip_tooltipContainer (у чекбокса согласия на рассылку)
    ACCOUNT_TYPE_HINT_WINDOW = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]")

    ACCOUNT_TYPE_HINT_WINDOW_TITLE = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]/descendant::*[contains(@class, 'UserView_title')]")

    ACCOUNT_TYPE_HINT_WINDOW_TEXT = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'ContextHelp_tooltip_')]/descendant::*[contains(@class, 'UserView_description')]")

    @staticmethod
    def INN_ERROR(language):
        return By.XPATH, f"//*[@role='alert' and preceding-sibling::*[text()='{page_text[language]['INN']}']]"

    OFFER_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::*[contains(@class, 'registration_offerDesc__')]]"
    )

    SUBMIT_BUTTON = (By.XPATH, f"//*[@data-testid='create-button']")

    OFFER_CHECKBOX = (By.NAME, "offer")

    # Нужен такой сложный селектор, чтобы нормально отслеживать чекбокс
    @staticmethod
    def CHECKBOX_IS_CHECKED_OR_NOT(checkbox, state):
        return (By.XPATH, f"//label[contains(@class, 'vkuiCheckbox') and .//*[text()='{checkbox}']]//*[contains(@class, 'vkuiCheckbox__icon--{state}')]")

    OFFER_TERMS_LINK = (By.XPATH, "//a[contains(@href, 'documents/offer')]")

    ORD_DOCS_LINK = (By.XPATH, "//a[contains(@href, 'ord_clients')]")

    TOS_LINK = (By.XPATH, "//a[contains(@href, 'adsvk/terms')]")

    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(@href, 'privacy')]")

    @staticmethod
    def MAILING_CHECKBOX(language): 
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__input') and following-sibling::*[descendant::*[contains(., '{page_text[language]['MAILING']}')]]]"

    @staticmethod
    def MAILING_CHECKBOX_HINT(language): 
        return By.XPATH, f"//*[contains(@class, 'Hint_hintTrigger') and preceding-sibling::*[contains(., '{page_text[language]['MAILING']}')]]"
    
    CREATE_CABINET_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")
    
    MAILING_CHECKBOX_HINT_WINDOW = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer') and contains(@class, 'registration_hint_')]")