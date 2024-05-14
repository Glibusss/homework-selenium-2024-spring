from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.help_page_locators import HelpPageLocators


class HelpPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = HelpPageLocators()

    TIP_LIST = ['Кейсы компаний', 'Справка', 'Форум идей', 'Задать вопрос']

    def click_help_cell(self):
        self.click(self.locators.HELP_CELL)

    def tooltip_became_visible(self):
        return self.became_visible(self.locators.HELP_TOOLTIP)
    
    def tooltip_became_invisible(self):
        return self.became_invisible(self.locators.HELP_TOOLTIP)

    def cells_became_visible(self):
        for t in self.TIP_LIST:
            if not self.became_visible(self.locators.TIP_NAME(t)):
                return False
        return True

    def click_cases_tip(self):
        self.click(self.locators.TIP_NAME('Кейсы компаний'))

    def click_help_tip(self):
        self.click(self.locators.TIP_NAME('Справка'))

    def click_forum_tip(self):
        self.click(self.locators.TIP_NAME('Форум идей'))

    def click_ask_tip(self):
        self.click(self.locators.TIP_NAME('Задать вопрос'))

    def iframe_became_visible(self):
        return self.became_visible(self.locators.IFRAME)
    