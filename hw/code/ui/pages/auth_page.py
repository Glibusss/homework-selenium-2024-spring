from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators
import time


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login_mail_ru(self, login, password):
        self.click(self.locators.MAIL_RU_AUTH_BUTTON)
        time.sleep(1)

        login_input = self.find(self.locators.MAIL_RU_LOGIN)
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)
        time.sleep(1)

        password_input = self.find(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)

    def login_regular(self, login, password):
        login_input = self.find(self.locators.REGULAR_LOGIN)
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.REGULAR_LOGIN_NEXT_BUTTON)
        time.sleep(1)

        password_input = self.find(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.REGULAR_LOGIN_NEXT_BUTTON)
        time.sleep(1)

    def login_to_new_cabinet(self, login, password):
        login_input = self.find(self.locators.MAIL_RU_LOGIN)
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)
        time.sleep(1)

        password_input = self.find(self.locators.MAIL_RU_PASSWORD)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)
        time.sleep(1)