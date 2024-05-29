from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class PollPageLocators(BasePageLocators):

    LEAD_FORMS_AND_POLLS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSimpleCell')]//*[text()='Лид-формы и опросы']",
    )

    POLLS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTabsItem')]//*[text()='Опросы']",
    )

    POLL_CREATE_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Surveys_createButton__')]",
    )

    POLL_MODAL_WINDOW = (
        By.XPATH,
        "//*[contains(@class, 'CreateSurveyModal_modalHeaderTitle__')]",
    )

    POLL_NAME = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите название')]",
    )

    UPLOAD_LOGO = (
        By.XPATH,
        "//*[text()='Загрузить логотип']",
    )

    CONTENT_MODAL_WINDOW = (
        By.XPATH,
        "//*[contains(@class, 'ModalSidebarPage_header__')]//*[text()='Медиатека']",
    )

    IMAGE_LOGO = (
        By.XPATH,
        "//*[contains(@class, 'ItemList_content__')]",
    )

    COMPANY_NAME = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите название компании')]",
    )

    POLL_HEADER = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите заголовок')]",
    )

    POLL_DESCRIPTION = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTextarea__') and contains(@placeholder, 'Введите описание опроса')]",
    )

    NEXT_POLL_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton') and contains(@data-testid, 'submit')]",
    )

    ADD_QUESTION_BUTTON = (
        By.XPATH,
        "//*[text()='Добавить вопрос']",
    )

    ADD_ANSWER_BUTTON = (
        By.XPATH,
        "//*[text()='Добавить вариант']",
    )

    POLL_QUESTION = (
        By.XPATH,
        "//*[contains(@class, 'Question_questionWrapper__')]",
    )

    QUESTION_TEXT_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTextarea__') and contains(@placeholder, 'Текст вопроса')]",
    )

    ANSWER_TEXT_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите ответ')]",
    )

    POLL_RESULT_HEADER = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите заголовок')]",
    )

    POLL_RESULT_DESCRIPTION = (
        By.XPATH,
        "//*[contains(@class, 'vkuiInput__') and contains(@placeholder, 'Введите описание: например, поблагодарите за прохождение опроса')]",
    )

    @staticmethod
    def find_created_poll(name):
        return (
            By.XPATH,
            f"//*[text()='{name}']",
        )
