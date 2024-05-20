from base_case import BaseCase


class TestHeader(BaseCase):
    def test_header_render(self, header_before):
        assert header_before.header_became_visible()
        assert header_before.logo_became_visible()
        assert header_before.account_selector_became_visible()
        assert header_before.vk_id_became_visible()

    def test_logo_click(self, header_before):
        header_before.click_logo()
        assert self.is_opened("https://ads.vk.com/hq/registration")

    def test_account_dropdown_appears(self, header_before):
        header_before.click_account_selector()
        assert header_before.account_selector_dropdown_became_visible()

    def test_vk_id_popup(self, header_before):
        header_before.click_vk_id()
        assert header_before.vk_id_popup_became_visible()

    def test_cabinet_dropdown_render(self, header_before):
        header_before.click_account_selector()
        assert len(header_before.get_account_selector_accounts()) >= 1
        assert len(header_before.get_account_selector_selected_account()) == 1
        assert header_before.all_accounts_link_became_visible()

    def test_cabinet_dropdown_click_away(self, header_before):
        header_before.click_account_selector()
        header_before.click_header()
        assert header_before.account_selector_dropdown_became_invisible()

    def test_cabinet_dropdown_all_cabinets(self, header_before):
        header_before.click_account_selector()
        assert header_before.all_accounts_link_became_visible()
        header_before.click_all_accounts_link()
        assert self.is_opened("https://ads.vk.com/hq/registration")
