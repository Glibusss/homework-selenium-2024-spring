from ui.pages.base_page import BasePage
from ui.locators.poll_page_locators import PollPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
)
import time


class PollPage(BasePage):
    locators = PollPageLocators
    url = "https://ads.vk.com/hq/overview"

    def _paste_text_by_locator(self, locator, text: str):
        input = self.find(locator)
        input.clear()
        input.send_keys(text)

    def _paste_text(self, input, text: str):
        input.clear()
        input.send_keys(text)

    def _compare_text_by_locator(self, locator, text: str) -> bool:
        input = self.find(locator)
        value = input.get_attribute("value")
        return value == text

    def go_to_lead_forms_page(self):
        self.click(PollPageLocators.LEAD_FORMS_AND_POLLS_BUTTON)

    def go_to_poll_page(self):
        self.click(PollPageLocators.POLLS_BUTTON)

    def open_poll_modal_window(self):
        try:
            self.click(PollPageLocators.POLL_CREATE_BUTTON)
        except StaleElementReferenceException:
            # JS что-то делает с этим элементом, поэтому ссылка не него может потеряться, следовательно, если это происходит, немного ждём и снова взаимодействуем с элементом
            self.became_visible(PollPageLocators.POLL_CREATE_BUTTON)
            self.click(PollPageLocators.POLL_CREATE_BUTTON)

    def paste_poll_appearance_stage(self, text):
        self._paste_text_by_locator(PollPageLocators.POLL_NAME, text[0])
        self._paste_text_by_locator(PollPageLocators.COMPANY_NAME, text[1])
        self._paste_text_by_locator(PollPageLocators.POLL_HEADER, text[2])
        self._paste_text_by_locator(PollPageLocators.POLL_DESCRIPTION, text[3])

    def set_up_logo(self):
        try:
            self.click(PollPageLocators.UPLOAD_LOGO)
        except StaleElementReferenceException:
            # JS что-то делает с этим элементом, поэтому он может быть некликабельным, следовательно, если это происходит, немного ждём и снова взаимодействуем с элементом
            self.click(PollPageLocators.POLL_CREATE_BUTTON)
        finally:
            self.became_visible(PollPageLocators.IMAGE_LOGO)
            self.click(PollPageLocators.IMAGE_LOGO)
            self.became_invisible(PollPageLocators.IMAGE_LOGO)

    def go_to_the_next_poll_stage(self):
        self.click(PollPageLocators.NEXT_POLL_BUTTON)

    def set_up_questions_page(self, questions_and_answers):
        self.click(PollPageLocators.ADD_QUESTION_BUTTON)
        self.find_all(PollPageLocators.ADD_ANSWER_BUTTON)[-1].click()
        questions = list(questions_and_answers.keys())
        answers = list(questions_and_answers.values())
        poll_questions = self.find_all(PollPageLocators.POLL_QUESTION)
        for i in range(len(poll_questions)):
            question_input = poll_questions[i].find_element(By.TAG_NAME, "textarea")
            self._paste_text(question_input, questions[i])
            question_answer_inputs = poll_questions[i].find_elements(
                By.TAG_NAME, "input"
            )
            for j in range(len(question_answer_inputs)):
                self._paste_text(question_answer_inputs[j], answers[i][j])

    def set_up_result_page(self, head_and_description):
        self._paste_text_by_locator(
            PollPageLocators.POLL_RESULT_HEADER, head_and_description[0]
        )
        self._paste_text_by_locator(
            PollPageLocators.POLL_RESULT_DESCRIPTION, head_and_description[1]
        )

    def open_poll(self, name):
        locator = PollPageLocators.find_created_poll(name)
        try:
            self.click(locator)
        except StaleElementReferenceException:
            # JS что-то делает с этим элементом, поэтому ссылка не него может потеряться, следовательно, если это происходит, немного ждём и снова взаимодействуем с элементом
            self.became_visible(locator)
            self.click(locator)

    def check_description_page(self, text):
        checks = []
        checks.append(
            self._compare_text_by_locator(PollPageLocators.POLL_NAME, text[0])
        )
        checks.append(
            self._compare_text_by_locator(PollPageLocators.COMPANY_NAME, text[1])
        )
        checks.append(
            self._compare_text_by_locator(PollPageLocators.POLL_HEADER, text[2])
        )
        checks.append(
            self._compare_text_by_locator(PollPageLocators.POLL_DESCRIPTION, text[3])
        )
        return all(checks)

    def check_questions_page(self, questions_and_answers):
        checks = []
        questions = list(questions_and_answers.keys())
        answers = list(questions_and_answers.values())
        poll_questions = self.find_all(PollPageLocators.POLL_QUESTION)
        for i in range(len(poll_questions)):
            question_input = poll_questions[i].find_element(By.TAG_NAME, "textarea")
            checks.append(question_input.get_attribute("value") == questions[i])
            question_answer_inputs = poll_questions[i].find_elements(
                By.TAG_NAME, "input"
            )
            for j in range(len(question_answer_inputs)):
                checks.append(
                    question_answer_inputs[j].get_attribute("value") == answers[i][j]
                )
        return all(checks)

    def check_result_page(self, head_and_description):
        checks = []
        checks.append(
            self._compare_text_by_locator(
                PollPageLocators.POLL_RESULT_HEADER, head_and_description[0]
            )
        )
        checks.append(
            self._compare_text_by_locator(
                PollPageLocators.POLL_RESULT_DESCRIPTION, head_and_description[1]
            )
        )
        return all(checks)
