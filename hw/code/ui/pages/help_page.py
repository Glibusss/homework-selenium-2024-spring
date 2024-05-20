from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.help_page_locators import HelpPageLocators


class HelpPage(BasePage):
    url = "https://ads.vk.com/hq/overview"
    locators = HelpPageLocators()

    TIP_LIST = ["Кейсы компаний", "Справка", "Форум идей", "Задать вопрос"]

    def click_help_cell(self):
        self.click(self.locators.HELP_CELL)

    def tooltip_with_content_became_visible(self):
        return self.became_visible(self.locators.HELP_TOOLTIP)

    def tooltip_became_invisible(self):
        return self.became_invisible(self.locators.HELP_TOOLTIP)

    def tips_with_content_became_visible(self):
        for t in self.TIP_LIST:
            if not self.became_visible(self.locators.TIP_NAME(t)):
                return False
        return True

    def click_cases_tip(self):
        self.click(self.locators.TIP_NAME(self.TIP_LIST[0]))

    def click_help_tip(self):
        self.click(self.locators.TIP_NAME(self.TIP_LIST[1]))

    def click_forum_tip(self):
        self.click(self.locators.TIP_NAME(self.TIP_LIST[2]))

    def click_ask_tip(self):
        self.click(self.locators.TIP_NAME(self.TIP_LIST[3]))

    def iframe_became_visible(self):
        return self.became_visible(self.locators.IFRAME)
    