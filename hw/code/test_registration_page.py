from base_case import BaseCase
from ui.locators.registration_page_locators import page_text

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
        assert registration_page.account_type_label_became_visible(current_language)

    def test_import_page_rendering(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        current_language = registration_page.get_selected_language()
        current_account_type = registration_page.get_selected_account_switch()
        assert registration_page.header_became_visible()
        assert registration_page.language_switch_became_visible()
        assert registration_page.back_button_became_visible()
        assert registration_page.account_type_switch_became_visible()
        benefits = registration_page.get_account_type_benefits()
        assert len(list(benefits)) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[0]
            assert benefit[1] == page_text[current_language][current_account_type][i]['title']
            assert benefit[2] == page_text[current_language][current_account_type][i]['desc']
        assert registration_page.import_continue_button_became_visible()
        assert registration_page.import_continue_note_became_visible()

    def test_import_page_account_switch_to_agency(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        current_language = registration_page.get_selected_language()
        current_account_type = registration_page.get_selected_account_switch()
        registration_page.switch_account_type(page_text[current_language]['AGENCY_DATIVE'])
        new_account_type = registration_page.get_selected_account_switch()
        assert current_account_type != new_account_type
        benefits = registration_page.get_account_type_benefits()
        assert len(benefits) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[0]
            assert benefit[1] == page_text[current_language][new_account_type][i]['title']
            assert benefit[2] == page_text[current_language][new_account_type][i]['desc']

    def test_import_page_account_switch_to_advertiser(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        current_language = registration_page.get_selected_language()
        current_account_type = registration_page.get_selected_account_switch()
        registration_page.switch_account_type(page_text[current_language]['AGENCY_DATIVE'])
        registration_page.switch_account_type(page_text[current_language]['ADVERTISER_DATIVE'])
        new_account_type = registration_page.get_selected_account_switch()
        assert current_account_type == new_account_type
        benefits = registration_page.get_account_type_benefits()
        assert len(benefits) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[0]
            assert benefit[1] == page_text[current_language][new_account_type][i]['title']
            assert benefit[2] == page_text[current_language][new_account_type][i]['desc']
        
    def test_import_page_switch_same_advertiser(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        current_account_type = registration_page.get_selected_account_switch()
        current_benefits = registration_page.get_account_type_benefits()
        registration_page.switch_account_type_by_value(current_account_type)
        new_benefits = registration_page.get_account_type_benefits()
        assert current_benefits == new_benefits

    def test_import_page_switch_same_agency(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        current_language = registration_page.get_selected_language()
        registration_page.switch_account_type(page_text[current_language]['AGENCY_DATIVE'])
        current_account_type = registration_page.get_selected_account_switch()
        current_benefits = registration_page.get_account_type_benefits()
        registration_page.switch_account_type_by_value(current_account_type)
        new_benefits = registration_page.get_account_type_benefits()
        assert current_benefits == new_benefits

    def test_continue_import(self, registration_page):
        registration_page.click_import_mytarget_cabinet_button()
        registration_page.click_import_continue_button()
        assert self.is_opened(url='target.my.com')
        