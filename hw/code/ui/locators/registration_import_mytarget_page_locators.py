from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

page_text = {
    'Русский': {
        'BACK_BUTTON': 'Назад',
        'IMPORT_PAGE_TITLE': 'Импорт рекламного кабинета myTarget',
        'IMPORT_PAGE_SUBTITLE': 'Далее потребуется войти в рекламный кабинет myTarget и предоставить VK Рекламе доступ к нему:',
        'ACCOUNT_TYPE': 'Тип аккаунта',
        'ADVERTISER_DATIVE': 'Рекламодателю',
        'AGENCY_DATIVE': 'Агентству',
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
        'CONTINUE': 'Продолжить',
        'CONTINUE_DESC': 'На следующем шаге нужно будет войти в кабинет myTarget и дать нужные разрешения VK Рекламе',            
    },
    'English': {
        'BACK_BUTTON': 'Back',
        'IMPORT_PAGE_TITLE': 'Import of myTarget ad account',
        'IMPORT_PAGE_SUBTITLE': 'Next, you will need to log in to myTarget account and grant VK Ads access to it:',
        'ACCOUNT_TYPE': 'Account type',
        'ADVERTISER_DATIVE': 'Advertiser',
        'AGENCY_DATIVE': 'Agency',
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
        'CONTINUE': 'Continue',
        'CONTINUE_DESC': 'In the next step, you will need to enter the myTarget account and give the necessary permissions to VK Advertising',    
    },
}

class RegistrationImportMytargetPageLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    REGISTRATION_IMAGE = (By.XPATH, "//*[contains(@class, 'registration_img')]")

    LANGUAGE_SWITCH = (By.XPATH, "//*[contains(@class, 'LanguageSelector')]")

    BACK_BUTTON = (By.XPATH, "//button[@data-testid='back-button']")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")

    ACCOUNT_TYPE_SWITCH = (By.XPATH, "//*[contains(@class, 'ImportPanel_panelSubTitle')]/descendant::*[contains(@class, 'vkuiSegmentedControl__in')]")

    @staticmethod
    def ACCOUNT_TYPE_BUTTON(account_type):
        return By.XPATH, f"//*[contains(@class, 'vkuiRadio__title')]//span[text()='{account_type}']"

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