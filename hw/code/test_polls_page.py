from base import BaseCase
import uuid
import time
import copy


class TestPollPage(BaseCase):

    LEAD_FORMS_LINK = "https://ads.vk.com/hq/leadads"

    POLLS_LINK = "https://ads.vk.com/hq/leadads/surveys"

    UNIQUE_POLL_NAME = str(uuid.uuid4())

    POLL_DESCRIPTION = [
        UNIQUE_POLL_NAME,
        "МГТУ",
        "Опрос по вычислительно гидродинамике",
        "Проверка базовых знаний по вычислительной гидродинамике",
    ]

    QUESTIONS_AND_ANSWERS = {
        "Какая форма расчётной сетки обладает min численной диффузией": [
            "Многогранная",
            "Прямоугольная",
        ],
        "Какие модели многофазности менее требовательны к сетке": [
            "Euler-Euler (EMP)",
            "Volume of Fluid (VOF)",
            "Mixture Multiphase (MMP)",
        ],
    }

    HEAD_AND_DESCRIPTION = ["Спасибо за ответы!", "Ответы получены :)"]

    def test_poll_page(self, poll_page):
        poll_page.go_to_lead_forms_page()
        assert self.is_opened(self.LEAD_FORMS_LINK)
        poll_page.go_to_poll_page()
        assert self.is_opened(self.POLLS_LINK)
        poll_page.open_poll_modal_window()
        poll_page.set_up_logo()
        poll_page.paste_poll_appearance_stage(self.POLL_DESCRIPTION)
        poll_page.go_to_the_next_poll_stage()
        poll_page.set_up_questions_page(self.QUESTIONS_AND_ANSWERS)
        poll_page.go_to_the_next_poll_stage()
        poll_page.set_up_result_page(self.HEAD_AND_DESCRIPTION)
        poll_page.go_to_the_next_poll_stage()
        poll_page.open_poll(self.UNIQUE_POLL_NAME)
        assert poll_page.check_description_page(self.POLL_DESCRIPTION)
        poll_page.go_to_the_next_poll_stage()
        assert poll_page.check_questions_page(self.QUESTIONS_AND_ANSWERS)
        poll_page.go_to_the_next_poll_stage()
        assert poll_page.check_result_page(self.HEAD_AND_DESCRIPTION)
        poll_page.go_to_the_next_poll_stage()
