import time
from base_case import BaseCase


class TestSettingsAccessPage(BaseCase):

    def test_is_access_settings_page_opened(self, settings_access_page):
        assert settings_access_page.has_header_and_sign_content()
        assert settings_access_page.add_button_became_visible()

    def test_is_modal_opened(self, settings_access_page):
        settings_access_page.click_add_button()
        assert settings_access_page.add_modal_became_visible()

    def test_is_on_more_click_redirected(self, settings_access_page):
        settings_access_page.click_more_link()
        settings_access_page.go_to_new_tab()
        assert self.is_opened("https://ads.vk.com/help/articles/additionalaccounts")

