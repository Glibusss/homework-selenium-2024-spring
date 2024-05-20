import time
from base_case import BaseCase


class TestHelpPage(BaseCase):

    def test_is_help_tooltip_opened(self, help_page):
        help_page.click_help_cell()
        assert help_page.tooltip_became_visible()
        assert help_page.tips_with_content_became_visible()

    def test_is_help_tooltip_closed(self, help_page):
        help_page.click_help_cell()
        help_page.click_help_cell()
        assert help_page.tooltip_became_invisible()

    def test_is_iframe_became_visible(self, help_page):
        help_page.click_help_cell()
        help_page.click_ask_tip()
        assert help_page.iframe_became_visible()

    def test_is_on_cases_tip_click_redirected(self, help_page):
        help_page.click_help_cell()
        help_page.click_cases_tip()
        help_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/cases")

    def test_is_on_help_tip_click_redirected(self, help_page):
        help_page.click_help_cell()
        help_page.click_help_tip()
        help_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/help")

    def test_is_on_forum_tip_click_redirected(self, help_page):
        help_page.click_help_cell()
        help_page.click_forum_tip()
        help_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/upvote")
        