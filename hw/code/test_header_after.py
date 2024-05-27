from base_case import BaseCase


class TestHeader(BaseCase):
    def test_header_render(self, header_after):
        assert header_after.header_became_visible()
        assert header_after.logo_became_visible()
        assert header_after.account_selector_became_visible()
        assert header_after.balance_became_visible()
        assert header_after.notifications_became_visible()
        assert header_after.vk_id_became_visible()

    def test_logo_click(self, header_after):
        header_after.click_logo()
        assert self.is_opened("https://ads.vk.com/hq/overview")

    def test_account_dropdown_appears(self, header_after):
        header_after.click_account_selector()
        assert header_after.account_selector_dropdown_became_visible()

    def test_balance_modal_appears(self, header_after):
        header_after.click_balance()
        assert header_after.balance_modal_became_visible()
        assert header_after.balance_modal_close_became_visible()

    def test_balance_modal_close_button(self, header_after):
        header_after.click_balance()
        header_after.click_balance_modal_close()
        assert header_after.balance_modal_became_invisible()

    def test_notification_popup_appears(self, header_after):
        header_after.click_notifications()
        assert header_after.notifications_popup_became_visible()
        assert header_after.notifications_settings_became_visible()

    def test_notification_popup_click_away(self, header_after):
        header_after.click_notifications()
        header_after.click_header()
        assert header_after.notifications_popup_became_invisible()
        assert header_after.notifications_settings_became_invisible()

    def test_click_notification_settings(self, header_after):
        header_after.click_notifications()
        header_after.click_notification_settings()
        assert header_after.notifications_settings_popup_became_visible()

    def test_vk_id_popup(self, header_after):
        header_after.click_vk_id()
        assert header_after.vk_id_popup_became_visible()

    def test_cabinet_dropdown_render(self, header_after):
        header_after.click_account_selector()
        assert len(header_after.get_account_selector_accounts()) >= 1
        assert len(header_after.get_account_selector_selected_account()) == 1
        assert header_after.all_accounts_link_became_visible()

    def test_cabinet_dropdown_click_away(self, header_after):
        header_after.click_account_selector()
        header_after.click_header()
        assert header_after.account_selector_dropdown_became_invisible()

    def test_cabinet_dropdown_all_cabinets(self, header_after):
        header_after.click_account_selector()
        assert header_after.all_accounts_link_became_visible()
        header_after.click_all_accounts_link()
        assert self.is_opened("https://ads.vk.com/hq/settings/access")
