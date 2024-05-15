from ui.pages.base_page import BasePage
from ui.locators.upvote_page_locators import UpvotePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class UpvotePage(BasePage):
    locators = UpvotePageLocators()
    url = "https://ads.vk.com/upvote"

    def click_search_field(self):
        self.scroll_and_click(self.locators.IDEAS_SEARCH_INPUT)

    def search_idea(self, text: str):
        input = self.find(self.locators.IDEAS_SEARCH_INPUT, timeout=10)
        input.clear()
        input.send_keys(text)
        input.send_keys(Keys.ENTER)

    def click_comment_button(self):
        self.scroll_and_click(self.locators.IDEA_COMMENTS_BUTTON, timeout=10)

    def get_idea_comments_count(self) -> int:
        return len(self.find_all(self.locators.COMMENT_CELL, timeout=10))

    def get_idea_comments_count_from_button(self) -> str:
        return self.find(self.locators.IDEA_COMMENTS_BUTTON).text

    def copy_firts_idea_link(self) -> str:
        self.click(self.locators.LINK_COPY_BUTTON)

    def get_first_idea_link_from_title(self) -> str:
        return self.find(self.locators.IDEA_LINK).get_attribute("href")

    def get_first_idea_id(self):
        date_and_id = self.find(self.locators.IDEA_DATE_AND_ID).text.split()
        return date_and_id[len(date_and_id) - 1]

    def paste_to_input(self):
        input = self.find(self.locators.IDEAS_SEARCH_INPUT)
        input.clear()
        input.send_keys(Keys.CONTROL + "v")

    def get_value_from_input(self) -> str:
        return self.find(self.locators.IDEAS_SEARCH_INPUT).get_attribute("value")

    def click_new_idea_button(self):
        self.scroll_and_click(self.locators.ADD_IDEA_BUTTON)

    def close_new_idea_modal_window(self):
        self.click(self.locators.CLOSE_IDEA_BUTTON)

    def modal_window_is_visible(self) -> bool:
        return self.is_visible(self.locators.CLOSE_IDEA_BUTTON)

    def modal_window_is_invisible(self) -> bool:
        return self.is_invisible(self.locators.CLOSE_IDEA_BUTTON)

    def get_first_idea_theme(self) -> str:
        return self.find(self.locators.IDEA_THEME).text

    def get_first_idea_status(self) -> str:
        return self.find(self.locators.IDEA_STATUS).text

    def click_cancel_filter_button(self) -> str:
        self.click(self.locators.CANCEL_FILTER_BUTTON)

    def open_themes_filter(self):
        self.click(self.locators.IDEAS_THEME_FILTER_BUTTON)

    def open_statuses_filter(self):
        self.click(self.locators.STATUS_FILTER_BUTTON)

    def get_all_idea_statuses(self):
        statuses = list()
        for status in self.find_all(self.locators.IDEA_STATUS, timeout=10):
            statuses.append(status.text)
        return statuses

    def get_all_idea_themes(self):
        themes = list()
        for card in self.find_all(self.locators.IDEA_CARD):
            card_themes = list()
            for theme in card.find_elements(
                By.CLASS_NAME, self.locators.IDEA_THEME_CLASSNAME_IN_CARD
            ):
                card_themes.append(theme.text)
            themes.append(card_themes)
        return themes

    def get_all_idea_titles(self):
        titles = list()
        for el in self.find_all(self.locators.IDEA_TITLE, timeout=10):
            titles.append(el.text)
        return titles

    def set_filter(self, new_filter: str):
        self.click(self.locators.DROPDOWN_MENU_ITEM(new_filter))
