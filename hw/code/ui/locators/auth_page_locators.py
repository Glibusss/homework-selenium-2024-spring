from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class AuthPageLocators(BasePageLocators):
    MAIL_RU_AUTH_BUTTON = (By.XPATH, "//*[@data-test-id='oAuthService_mail_ru']")
    MAIL_RU_LOGIN = (By.NAME, 'username')
    MAIL_RU_PASSWORD = (By.NAME, "password")
    MAIL_RU_NEXT_BUTTON = (By.XPATH, "//*[@data-test-id='next-button']")
    MAIL_RU_SUBMIT_BUTTON = (By.XPATH, "//*[@data-test-id='submit-button']")

    REGULAR_LOGIN = (By.NAME, 'login')
    REGULAR_LOGIN_NEXT_BUTTON = (By.XPATH, "//button[@type='submit' and descendant::span[text()='Продолжить' or text()='Continue']]")
    CREATE_NEW_PROFILE_BUTTON = (By.XPATH, "//*[@data-test-id='addOrganizationButton']")