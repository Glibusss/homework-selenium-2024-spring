import time
from base_case import BaseCase


class TestSettingsNotificationsPage(BaseCase):

    def test_is_notifications_settings_page_opened(self, settings_notifications_page):
        assert settings_notifications_page.has_h2_content_title()
        assert settings_notifications_page.has_checkbox_content()
        assert settings_notifications_page.has_switch_email_content()
        assert settings_notifications_page.has_telegram_cell_content()

    def test_is_save_modal_became_visible_switch_click(
        self, settings_notifications_page
    ):
        settings_notifications_page.click_switch()
        assert settings_notifications_page.has_save_modal_content()

    def test_is_save_modal_became_visible_checkbox_click(
        self, settings_notifications_page
    ):
        settings_notifications_page.click_checkbox()
        assert settings_notifications_page.has_save_modal_content()

    def test_is_on_checkbox_click_checkbox_changed(self, settings_notifications_page):
        checked = settings_notifications_page.checkbox_checked()
        settings_notifications_page.click_checkbox()

        if checked:
            assert settings_notifications_page.checkbox_not_checked()
        else:
            assert settings_notifications_page.checkbox_checked()

    def test_is_on_cancel_click_checkbox_returned(self, settings_notifications_page):
        checked = settings_notifications_page.checkbox_checked()
        settings_notifications_page.click_checkbox()
        settings_notifications_page.click_cancel()

        if checked:
            assert settings_notifications_page.checkbox_checked()
        else:
            assert settings_notifications_page.checkbox_not_checked()

    def test_is_on_save_click_checkbox_saved(self, settings_notifications_page):
        checked = settings_notifications_page.checkbox_checked()
        print(checked)
        settings_notifications_page.click_checkbox()
        settings_notifications_page.click_save()

        if checked:
            assert settings_notifications_page.checkbox_not_checked()
        else:
            assert settings_notifications_page.checkbox_checked()

