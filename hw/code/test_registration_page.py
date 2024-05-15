from base_case import BaseCase

class TestRegistrationPage(BaseCase):
    def test_main_page_rendering(self, registration_page):
        assert registration_page.header_became_visible()
        assert registration_page.language_switch_became_visible()
        assert registration_page.main_page_title_became_visible()
        assert registration_page.main_page_subtitle_became_visible()
        assert registration_page.create_new_cabinet_button_became_visible()
        assert registration_page.import_mytarget_cabinet_button_became_visible()

    def test_main_page_mytarget_hint(self, registration_page):
        registration_page.hover_import_mytarget_cabinet_button_hint()
        assert registration_page.mytarget_hint_became_visible()

    def test_create_new_cabinet_button(self, registration_page):
        registration_page.click_create_new_cabinet_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/new')

    def test_import_mytarget_cabinet_button(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        assert self.is_opened('https://ads.vk.com/hq/registration/import/target')

    def test_create_page_rendering(self, registration_page):
        registration_page.click_create_new_cabinet_button()
        current_language = registration_page.get_selected_language()
        assert registration_page.header_became_visible()
        assert registration_page.language_switch_became_visible()
        assert registration_page.back_button_became_visible()
        assert registration_page.create_page_title_became_visible(current_language)
        assert registration_page.account_ad_type_became_visible(current_language) != False