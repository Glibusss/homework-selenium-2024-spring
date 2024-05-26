from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class CampaignPageLocators(BasePageLocators):
    CREATE_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Создать кампанию']",
    )

    NAME_SIGN = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]")
    NAME_EDIT = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]//textarea")
    SUBMIT_NAME = (By.XPATH, "//*[contains(@class, 'EditableTitle_container__')]//svg")

    @staticmethod
    def NAME_CONTENT(name):
        return (By.XPATH, f"//*[contains(@class, 'EditableTitle_container__')]//*[text()='{name}]")
    
    TARGET_TABS = (By.XPATH, "//*[contains(@class, 'ObjectiveTabs_tabItemContent__') and text()='Целевые действия']")

    RECOGNITION_TABS = (By.XPATH, "//*[contains(@class, 'ObjectiveTabs_tabItemContent__') and text()='Узнаваемость и охват']")

    TARGET_TABS_SIGN = (By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Что будете рекламировать?']")

    RECOGNITION_TABS_SIGN = (By.XPATH, "//*[contains(@class, 'FormItem_topText__') and text()='Какой формат будете использовать?']")

    @staticmethod
    def CATEGORY_CELL(data_id, sign):
        return (By.XPATH, f"//*[contains(@data-id, '{data_id}')]//*[text()='{sign}']")

    SITE_NAME_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Рекламируемый сайт']]//input",
    )

    @staticmethod
    def ERROR_SITE_NAME(error):
        return (By.XPATH, f"//*[contains(@class, 'vkuiFormItem')]//*[text()='{error}']")

    BANNER = (By.XPATH, "//*[contains(@class, 'formBanner_container__')]//*[text()='Пиксель не установлен']")

    TARGET_ACTION_SELECT = (By.XPATH, "//*[contains(@data-testid, 'priced-goal')]")

    DROPDOWN_NAME = (By.XPATH, "//*[contains(@class, 'SelectOption_groupName__') and text()='ТРАФИК']")

    @staticmethod
    def DROPDOWN_OPTIONS(content):
        return (By.XPATH, f"//*[contains(@class, 'vkuiCustomSelectOption__children') and text()='{content}']")
    
    SWITCH_MAIN_SIGN = By.XPATH, "//*[@data-name='budgetOptimization']//*[text()='Оптимизация бюджета кампании']"
    SWITCH_ADDITIONAL_SIGN = By.XPATH, "//*[@data-name='budgetOptimization']//*[text()='Алгоритмы будут распределять средства кампании между всеми группами объявлений в пользу более эффективных.']"
    SWITCH_MORE = (By.XPATH, "//*[@href='https://ads.vk.com/help/articles/optimization' and text()='Подробнее']")
    SWITCH = (By.XPATH, "//input[@data-testid='budget-optimization']")


    STRATEGY_ACTION_SELECT = (By.XPATH, "//*[contains(@data-testid, 'autobidding-mode')]")

    BUDGET_INPUT = (By.XPATH, "//*[@data-testid='targeting-not-set']")

    BUDGET_PERIOD_SELECT = (By.XPATH, "//*[@data-testid='budget']")

    AMOUNT_TIP = (By.XPATH, "//*[text()='Не менее 100&nbsp;₽']")

    AMOUNT_ERROR = (By.XPATH, "//*[text()='Бюджет кампании должен быть не меньше 100₽']")

    START_DATE = (By.XPATH, "//*[@data-testid='start-date']")
    START_DATE_INPUT = (By.XPATH, "//*[@data-testid='start-date']//input")
    START_DATE_CROSS = (By.XPATH, "//*[@data-testid='start-date']//*[contains(@class, 'vkuiIconButton')]")

    END_DATE = (By.XPATH, "//*[@data-testid='end-date']")
    END_DATE_INPUT = (By.XPATH, "//*[@data-testid='end-date']//input")
    END_DATE_CROSS = (By.XPATH, "//*[@data-testid='end-date']//*[contains(@class, 'vkuiIconButton')]")

    CREATE_FOOTER = (By.XPATH, "//*[contains(@class, 'CreateFooter_footer__')]")
    CREATE_FOOTER_CONTINUE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Продолжить']")
    CREATE_FOOTER_SAVE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Сохранить как черновик']")
    CREATE_FOOTER_BACK = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Назад']")
    CREATE_FOOTER_DRAFTSTATUS = (By.XPATH, "//*[contains(@class, 'CreateFooter_draftStatus__') and text()='Изменения сохранены']")
    CREATE_FOOTER_ERROR = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='1 ошибка']")

    DRAFTS_BUTTON = (
    By.XPATH,
     "//*[contains(@class, 'vkuiButton__content') and text()='Черновики']",
    )

    TABLE_HEADER = (By.XPATH, "//*[contains(@class, 'BaseTable__header')]//*[@id='checkbox-all']")
    DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")

    DELETE_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]")
    DELETE_MODAL_HEADER = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[text()='Удалить выбранные черновики?']")
    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    MODAL_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[contains(@class, 'vkuiButton__content') and text()='Отмена']")
    MODAL_CANCEL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")
