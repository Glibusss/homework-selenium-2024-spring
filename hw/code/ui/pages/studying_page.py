from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.studying_page_locators import StudyingPageLocators


class StudyingPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = StudyingPageLocators()

    PR_OBJECTS_LIST = [
        "Сообщество ВКонтакте",
        "Каталог товаров",
        "Лид-формы",
        "Музыка",
        "Дзен",
        "Сайт",
        "Мобильное приложение",
        "VK Mini Apps",
        "Видео и трансляции",
    ]
    PR_METHODS_LIST = [
        "Создать каталог с подсказками",
        "Смотреть видеоурок от экспертов VK",
        "Смотреть курс на обучающей платформе",
    ]

    def click_studying_cell(self):
        self.click(self.locators.STUDY_CELL)

    def modal_became_visible(self):
        return self.became_visible(self.locators.CHOOSE_STUDYING_MODAL)

    def modal_became_invisible(self):
        return self.became_invisible(self.locators.CHOOSE_STUDYING_MODAL)

    def has_modal_header_content(self):
        return self.became_visible(
            self.locators.STUDYING_MODAL_H2
        ) and self.became_visible(self.locators.STUDYING_MODAL_H4)

    def has_modal_footer_content(self):
        return self.became_visible(
            self.locators.STUDYING_MODAL_FOOTER_SIGN
        ) and self.became_visible(self.locators.LATER_BUTTON)

    def has_choose_modal_content(self):
        for p in self.PR_OBJECTS_LIST:
            if not self.became_visible(self.locators.SOURCE_ITEM(p)):
                return False
        return True

    def close_button_became_visible(self):
        return self.became_visible(self.locators.CLOSE_BUTTON)

    def has_method_modal_header_content(self):
        return self.became_visible(self.locators.STUDYING_METHOD_MODAL_H2)

    def has_method_modal_content(self):
        for p in self.PR_METHODS_LIST:
            if not self.became_visible(self.locators.SOURCE_ITEM(p)):
                return False
        return True

    def video_iframe_became_visible(self):
        return self.became_visible(self.locators.IFRAME)

    def tips_became_visible(self):
        return (
            self.became_visible(self.locators.TIP)
            and self.became_visible(self.locators.SIDEBAR)
            and self.became_visible(self.locators.TIP_CLOSE)
        )

    def stop_onboarding_modal_became_visible(self):
        return self.became_visible(self.locators.STOP_ONBOARDING_MODAL)

    def has_stop_onboarding_modal_header_content(self):
        return self.became_visible(
            self.locators.TIP_CLOSE_MODAL_H2
        ) and self.became_visible(self.locators.TIP_CLOSE_MODAL_H4)

    def stop_onboarding_modal_buttons_became_visible(self):
        return self.became_visible(self.locators.BREAK_BUTTON) and self.became_visible(
            self.locators.CANCEL_BUTTON
        )

    def stop_onboarding_modal_became_invisible(self):
        return self.became_invisible(self.locators.STOP_ONBOARDING_MODAL)

    def click_catalog_cell(self):
        self.click(self.locators.SOURCE_ITEM("Каталог товаров"))

    def click_catalog_with_tips_cell(self):
        self.click(self.locators.SOURCE_ITEM("Создать каталог с подсказками"))

    def click_experts_cell(self):
        self.click(self.locators.SOURCE_ITEM("Смотреть видеоурок от экспертов VK"))

    def click_course_cell(self):
        self.click(self.locators.SOURCE_ITEM("Смотреть курс на обучающей платформе"))

    def click_close_tip(self):
        self.click(self.locators.TIP_CLOSE)

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

    def click_break_button(self):
        self.click(self.locators.BREAK_BUTTON)

    def click_close_button(self):
        self.click(self.locators.CLOSE_BUTTON)

    def click_later_button(self):
        self.click(self.locators.LATER_BUTTON)
