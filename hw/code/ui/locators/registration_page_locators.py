from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

page_text = {
    'Русский': {
        'MAIN_PAGE_TITLE': 'Добро пожаловать' \
                           'в VK Рекламу',
        'MAIN_PAGE_SUBTITLE': 'Перенесите настройки и кампании из существующего рекламного кабинета или создайте новый',
        'CREATE_CABINET': 'Создать новый кабинет',
        'IMPORT_MYTARGET': 'Использовать рекламный кабинет myTarget',
        'BACK_BUTTON': 'Назад',
        'CREATE_PAGE_TITLE': 'Регистрация кабинета',
        'ACCOUNT_TYPE': 'Тип аккаунта',
        'ADVERTISER_NOMINATIVE': 'Рекламодатель',
        'ADVERTISER_DATIVE': 'Рекламодателю',
        'AGENCY_NOMINATIVE': 'Агентство',
        'AGENCY_DATIVE': 'Агентству',
        'CHOOSE_COUNTRY': 'Выберите страну',
        'RUSSIA': 'Россия',
        'ARMENIA': 'Армения',
        'CURRENCY': 'Валюта',
        'RUBLE': 'Российский рубль (RUB)',
        'DOLLAR': 'Доллар США (USD)',
        'EURO': 'Евро (EUR)',
        'INDIVIDUAL': 'Физическое лицо',
        'INDIVIDUAL_HINT': 'Не требуется заключение договора. Доступные методы оплаты - банковская карта, электронные деньги, платеж со счета телефона.',
        'LEGAL_ENTITY': 'Юридическое лицо',
        'LEGAL_ENTITY_HINT': 'Потребуется предоставить реквизиты юридического лица. В конце каждого месяца клиенту предоставляется бухгалтерская отчётность. Доступные методы оплаты - банковский перевод для юридических лиц.',
        'INN': 'ИНН',
        'INN_EXAMPLE': 'Пример: 100303539843',
        'FULL_NAME': 'ФИО',
        'ACCEPT_CHECKBOX': 'Создавая кабинет, вы принимаете условия*',
        'OFFER': 'Оферты',
        'ORD': 'Соглашение о передаче рекламных данных',
        'TOS': 'Правила пользования сервисом',
        'PRIVACY': 'Политику конфиденциальности',
        'MAILING': 'Даю согласие на получение рассылок информационного и рекламно-информационного содержания',
        'MAILING_HINT': 'Соглашение регулирует получение уведомлений следующего характера:' \
                        '– сообщения ВКонтакте'
                        '– уведомления в разделе «Колокольчик» ВКонтакте'
                        '– email-рассылки'
                        '– push-уведомления'
                        '– звонки'
                        '– смс-сообщения',
        'advert': [
            {
                'title': 'Настройки аккаунта',
                'desc': 'Будут использованы настройки кабинета и реквизиты',
            },
            {
                'title': 'Мобильные приложения',
                'desc': 'Все мобильные приложения будут привязаны к новому кабинету',
            },
            {
                'title': 'Аудитории',
                'desc': 'Сможете использовать аудитории myTarget в кабинете VK Рекламы',
            },
            {
                'title': 'Кампании',
                'desc': 'Сможете копировать нужные кампании из myTarget в новый кабинет',
            },
            {
                'title': 'Товарные фиды',
                'desc': 'Cможете скопировать нужные товарные фиды в новый кабинет',
            },
        ],
        'agency': [
            {
                'title': 'Клиенты',
                'desc': 'Вы сможете работать с уже созданными клиентами и создавать новых',
            },
            {
                'title': 'Статистика',
                'desc': 'Вся статистика и все отчёты перенесутся из старого кабинета',
            },
            {
                'title': 'Настройки аккаунта',
                'desc': 'Будут использованы настройки кабинета и реквизиты',
            },
            {
                'title': 'Бюджет',
                'desc': 'Перенесётся бюджет из исходного кабинета',
            },
            {
                'title': 'Старый кабинет myTarget',
                'desc': 'Можно будет по-прежнему заходить в свой старый кабинет',
            },
        ],            
    },
    'English': {
        'MAIN_PAGE_TITLE': 'Welcome ' \
                           'to VK Ads',
        'MAIN_PAGE_SUBTITLE': 'Transfer settings and campaigns from an existing account or create a new one',
        'CREATE_CABINET': 'Create a new account',
        'IMPORT_MYTARGET': 'Use myTarget ad account',
        'BACK_BUTTON': 'Back',
        'CREATE_PAGE_TITLE': 'Account registration',
        'ACCOUNT_TYPE': 'Account type',
        'ADVERTISER_NOMINATIVE': 'Advertiser',
        'ADVERTISER_DATIVE': 'Advertiser',
        'AGENCY_NOMINATIVE': 'Agency',
        'AGENCY_DATIVE': 'Agency',
        'CHOOSE_COUNTRY': 'Choose a country',
        'RUSSIA': 'Russian Federation',
        'ARMENIA': 'Armenia',
        'CURRENCY': 'Currency',
        'RUBLE': 'Russian ruble (RUB)',
        'DOLLAR': 'U.S. dollar (USD)',
        'EURO': 'Euro (EUR)',
        'INDIVIDUAL': 'Individual',
        'INDIVIDUAL_HINT': 'You can easily open an individual account by accepting the T&Cs online.'
                            'Available payment methods: credit card, payment systems such as PayPal, etc.'
                            'Note: the account type cannot be changed after the account has been created.',
        'LEGAL_ENTITY': 'Legal entity',
        'LEGAL_ENTITY_HINT': 'This account type is mostly used for businesses with a legal entity.' 
                             'Available payment methods: credit card, payment systems such as PayPal, etc.'
                             'Note: the account type cannot be changed once the account has been created.',
        'INN': 'TIN',
        'INN_EXAMPLE': 'Example: 100303539843',
        'FULL_NAME': 'Full name',
        'ACCEPT_CHECKBOX': 'By creating an account you accept the terms*',
        'OFFER': 'Offer',
        'ORD': 'Advertising data transfer agreement',
        'TOS': 'Terms of use of the service',
        'PRIVACY': 'Privacy Policy',
        'MAILING': 'I agree to receive information and promotional newsletters',
        'MAILING_HINT': 'The agreement regulates the receipt of notifications such as:'
                        '– VK messages'
                        '– notifications in the "Bell" section of VK'
                        '– email notifications'
                        '– push notifications'
                        '– calls'
                        '– sms-messages',
        'advert': [
            {
                'title': 'Account settings',
                'desc': 'Account settings and details will be used',
            },
            {
                'title': 'Mobile applications',
                'desc': 'All mobile applications will be linked to the new account',
            },
            {
                'title': 'Audiences',
                'desc': 'You will be able to use myTarget audiences in your VK Advertising account',
            },
            {
                'title': 'Campaigns',
                'desc': 'You will be able to copy the necessary campaigns from myTarget to a new account',
            },
            {
                'title': 'Product feeds',
                'desc': 'You will be able to copy the necessary product feeds to the new account',
            },
        ],
        'agency': [
            {
                'title': 'Clients',
                'desc': 'You will be able to work with existing clients and create new ones',
            },
            {
                'title': 'Statistics',
                'desc': 'All statistics and all reports will be transferred from the old account',
            },
            {
                'title': 'Account settings',
                'desc': 'Account settings and details will be used',
            },
            {
                'title': 'Budget',
                'desc': 'The budget from the original office will be transferred',
            },
            {
                'title': 'Old myTarget account',
                'desc': 'You still will be able to log into your old account',
            },
        ],
    },
}

class RegistrationPageLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    MAIN_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'registration_panelTitle')]")
    
    MAIN_PAGE_SUBTITLE = (By.XPATH, "//*[contains(@class, 'registration_panelSubTitle')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'HeaderNav_headerLanguageSelector')]")

    CREATE_NEW_CABINET_BUTTON = (By.ID, "click-createNewButton")

    IMPORT_MYTARGET_CABINET_BUTTON = (By.ID, "click-exportMTButton")

    IMPORT_MYTARGET_CABINET_HINT = (By.XPATH, "//*[contains(@class, 'ContextHelp_tooltip')]")

    BACK_BUTTON = (By.XPATH, "//button[@data-testid='back-button']")

    CREATE_PAGE_TITLE = (By.XPATH, "//*[contains(@class, 'HeaderNav_headerFormTitle')]")

    # Выбираем нажимаемый элемент с радиобаттоном
    ACCOUNT_TYPE_BUTTON_ELEM = (By.XPATH, "//*[contains(@class, 'vkuiRadio') and contains(@class, 'vkuiTappable') and child::input[starts-with(@data-testid, 'cabinet-')]]")

    @staticmethod
    def ACCOUNT_TYPE_LABEL(language):
        return By.XPATH, f"//*[text()='{page_text[language]['ACCOUNT_TYPE']}']"

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")

    IMPORT_MYTARGET_CABINET_BUTTON_HINT = (By.XPATH, "//*[contains(@id, 'click-exportMTButton')]/descendant::*[contains(@class, 'Hint_hintTrigger')]")

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

    EMAIL_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::h5[text()='Email*']]"
    )

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//span[text()='{account_type}']"
        
    @staticmethod
    def ACCOUNT_TYPE_HINT(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]/descendant::*[preceding-sibling::span[text()='{account_type}']]/*[contains(@class, 'Hint_hintTrigger')]"
    
    ACCOUNT_TYPE_HINT_WINDOW = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer')]")

    ACCOUNT_TYPE_HINT_WINDOW_TITLE = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer')]/descendant::div[contains(@class, 'UserView_title')]")

    ACCOUNT_TYPE_HINT_WINDOW_TEXT = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer')]/descendant::div[contains(@class, 'UserView_description')]")

    @staticmethod
    def INN_ERROR(language):
        return By.XPATH, f"//*[@role='alert' and preceding-sibling::h5[text()='{page_text[language]['INN']}']]"

    OFFER_ERROR = (
        By.XPATH,
        "//*[@role='alert' and preceding-sibling::div[contains(@class, 'registration_offerDesc__')]]"
    )

    SUBMIT_BUTTON = (By.XPATH, f"//*[@data-testid='create-button']")

    OFFER_CHECKBOX = (By.NAME, "offer")

    OFFER_TERMS_LINK = (By.XPATH, "//a[contains(@href, 'offer_fl')]")

    ORD_DOCS_LINK = (By.XPATH, "//a[contains(@href, 'ord_clients')]")

    TOS_LINK = (By.XPATH, "//a[contains(@href, 'adsvk/terms')]")

    PRIVACY_POLICY_LINK = (By.XPATH, "//a[contains(@href, 'privacy')]")

    @staticmethod
    def MAILING_CHECKBOX(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiCheckbox__input') and following-sibling::*[descendant::span[contains(., '{page_text[language]['MAILING']}')]]]"

    @staticmethod
    def MAILING_CHECKBOX_HINT(language): 
        return By.XPATH, f"//*[contains(@class, 'Hint_hintTrigger') and preceding-sibling::span[contains(., '{page_text[language]['MAILING']}')]]"
    
    ACCOUNT_TYPE_SWITCH = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControl__in')]")

    @staticmethod
    def ACCOUNT_TYPE_SELECTOR_BY_TEXT(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[following-sibling::h4[text()='{account_type}']]"
    
    @staticmethod
    def ACCOUNT_TYPE_SELECTOR_BY_VALUE(value):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/*[@value='{value}']"
    
    SWITCH_SELECTED_ACCOUNT_TYPE = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControlOption--checked')]/descendant::input")

    SWITCH_SELECTED_ACCOUNT_LABEL = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControlOption--checked')]/descendant::h4")

    IMPORT_BENEFIT_ITEM = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCell_')]")

    IMPORT_BENEFIT_ICON = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCell')]/descendant::*[contains(@class, 'vkuiIcon')]")

    IMPORT_BENEFIT_ITEM_TITLE = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCellTitle')]")

    IMPORT_BENEFIT_ITEM_DESC = (By.XPATH, "//*[contains(@class, 'ImportPanel_grantCellDesc')]")

    IMPORT_CONTINUE_BUTTON = (By.XPATH, "//*[@data-testid='import-continue']")

    IMPORT_CONTINUE_DESC = (By.XPATH, "//*[contains(@class, 'ImportPanel_actionDesc')]")