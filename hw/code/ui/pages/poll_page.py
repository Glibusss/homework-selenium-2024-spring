from ui.pages.base_page import BasePage
from ui.locators.poll_page_locators import PollPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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

    def go_to_lead_forms_page(self):
        self.click(PollPageLocators.LEAD_FORMS_AND_POLLS_BUTTON)

    def go_to_poll_page(self):
        self.click(PollPageLocators.POLLS_BUTTON)

    def open_poll_modal_window(self):
        self.click(PollPageLocators.POLL_CREATE_BUTTON)

    def paste_poll_appearance_stage(self, text):
        self._paste_text_by_locator(PollPageLocators.POLL_NAME, text[0])
        self._paste_text_by_locator(PollPageLocators.COMPANY_NAME, text[1])
        self._paste_text_by_locator(PollPageLocators.POLL_HEADER, text[2])
        self._paste_text_by_locator(PollPageLocators.POLL_DESCRIPTION, text[3])

    def set_up_logo(self):
        self.click(PollPageLocators.UPLOAD_LOGO)
        self.click(PollPageLocators.IMAGE_LOGO)

    def go_to_the_next_poll_stage(self):
        self.click(PollPageLocators.NEXT_POLL_BUTTON)

    def set_up_questions_page(self, questions_and_answers: dict):
        self.click(PollPageLocators.ADD_QUESTION_BUTTON)
        self.find_all(PollPageLocators.ADD_ANSWER_BUTTON)[-1].click()
        questions = questions_and_answers.keys()
        answers = questions_and_answers.values()
        poll_questions = self.find_all(PollPageLocators.POLL_QUESTION)
        for i in range(len(poll_questions)):
            question_input = poll_questions[i].find_element(
                PollPageLocators.QUESTION_TEXT_INPUT
            )
            question_input.click()
            self._paste_text(question_input, questions[i])
            question_answers = poll_questions[i].find_elements(
                PollPageLocators.ANSWER_TEXT_INPUT
            )
            for j in range(len(questions_and_answers)):
                self._paste_text(question_answers[j], answers[i][j])
