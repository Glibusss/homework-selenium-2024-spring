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

    START_DATE = (By.XPATH, "//*[@data-testid='start-date']")
    START_DATE_INPUT = (By.XPATH, "//*[@data-testid='start-date']//input")

    END_DATE = (By.XPATH, "//*[@data-testid='end-date']")
    END_DATE_INPUT = (By.XPATH, "//*[@data-testid='end-date']//input")

    CREATE_FOOTER = (By.XPATH, "//*[contains(@class, 'CreateFooter_footer__')]")
    CREATE_FOOTER_CONTINUE = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Продолжить']")
    CREATE_FOOTER_PUBLISH = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Опубликовать']")

    @staticmethod
    def SECTION(name):
        return (By.XPATH, f"//*[contains(@class, 'GroupForm_groupHeader__')]//*[text='{name}']")
    
    @staticmethod
    def REGION_BUTTON(region):
        return (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='{region}']")
    
    @staticmethod
    def SELECTED_REGION_CELL(region):
        return (By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='{region}']")
    
    @staticmethod
    def GENDER_RADIO(gender):
        return (By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='{gender}]")
    
    @staticmethod
    def AGE_SELECT_CHECK(age):
        return (By.XPATH, f"//*[contains(@class, 'vkuiTypography') and text()='{age}']")
    
    PEGI_AGE_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='0+']")

    INTEREST_SUBSECTION = (By.XPATH, "//*[contains(@class, 'InterestsSubSection_headerText__')]")
    INTEREST_SELECT = (By.XPATH, "//*[@data-name='interests']//input")

    STOP_INTEREST_OPENER = (By.XPATH, "//*[contains(@class, 'Interests_negativeOpener__')]")

    STOP_INTEREST_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'vkuiTypography') and text()='Исключая интересы']]//input")

    DESKTOP_CHECKBOX = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Десктопные']")
    MOBILE_CHECKBOX = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Мобильные']")

    UPLOAD_AVATAR = (By.XPATH, "//*[contains(@class, 'UploadMediaButton_buttonLogoIcon__')]")
    TITLE_INPUT = (By.XPATH, "//input[contains(@name='заголовок, макс. 40 символов')]")
    SHORT_DESCRIPTION = (By.XPATH, "//textarea[@name='заголовок, макс. 90 символов']")
    LONG_DESCRIPTION = (By.XPATH, "//textarea[@name='Длинный текст для использования в лентах соцсетей (2000 знаков)']")
    BUTTON_TEXT_INPUT = (By.XPATH, "//input[contains(@name='Доп. заголовок 30 знаков')]")
    ADVERTISER_DESCRIPTION = (By.XPATH, "//textarea[@name='юридическая информация, макс. 115 символов']")

    MEDIATEC = (By.XPATH, "//*[@data-testid='set-global-image']")
    IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ImageItems_imageItem__')]")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit']")

    TABLE_HEADER = (By.XPATH, "//*[contains(@class, 'BaseTable__header')]//*[@id='checkbox-all']")

    DELETE_SELECT = (By.XPATH, "//*[@data-testid='select-options']")

    EDIT_TAPPABLE = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='Редактировать']")

    DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")

    DELETE_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]")
    DELETE_MODAL_HEADER = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[text()='Удалить выбранные черновики?']")
    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    @staticmethod
    def ENTITY_NAME_CELL(name):
        return (By.XPATH, f"//*[contains(@class, 'nameCellContent_link__') and text()='{name}']")
    
    PEGI_16_AGE_SELECT = (By.XPATH, "//*[contains(@class, 'vkuiTypography') and text()='16+']")

    @staticmethod
    def CHECKBOX_NAME_IS_CHECKED_OR_NOT(checkbox, state):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCheckbox') and .//* [contains(@class, 'vkuiTypography') and text()='{checkbox}']]//*[contains(@class, 'vkuiCheckbox__icon--{state}')]",
        )
    
    AVATAR_IMAGE = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_img__')]")

    MODAL_DELETE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[contains(@class, 'vkuiButton__content') and text()='Отмена']")
    MODAL_CANCEL_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]//*[contains(@class, 'vkuiButton__content') and text()='Удалить']")

