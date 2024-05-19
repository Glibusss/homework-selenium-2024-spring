from base_case import BaseCase
from ui.locators.registration_main_page_locators import page_text


class TestRegistrationMainPageLocalization(BaseCase):
    def test_main_page_russian(self, registration_main_page):
        assert registration_main_page.text_became_visible('Русский')
        assert registration_main_page.text_became_visible('English')
        registration_main_page.select_language('Русский')
        assert registration_main_page.text_became_visible(page_text['Русский']['MAIN_PAGE_TITLE'])
        assert registration_main_page.text_became_visible(page_text['Русский']['MAIN_PAGE_SUBTITLE'])
        assert registration_main_page.text_became_visible(page_text['Русский']['CREATE_CABINET'])
        assert registration_main_page.text_became_visible(page_text['Русский']['IMPORT_MYTARGET'])
        registration_main_page.hover_import_mytarget_cabinet_button_hint()
        for item in page_text['Русский']['IMPORT_MYTARGET_HINT_ITEMS']:
            assert registration_main_page.text_became_visible(item)

    def test_main_page_english(self, registration_main_page):
        assert registration_main_page.text_became_visible('Русский')
        assert registration_main_page.text_became_visible('English')
        registration_main_page.select_language('English')
        assert registration_main_page.text_became_visible(page_text['English']['MAIN_PAGE_TITLE'])
        assert registration_main_page.text_became_visible(page_text['English']['MAIN_PAGE_SUBTITLE'])
        assert registration_main_page.text_became_visible(page_text['English']['CREATE_CABINET'])
        assert registration_main_page.text_became_visible(page_text['English']['IMPORT_MYTARGET'])
        registration_main_page.hover_import_mytarget_cabinet_button_hint()
        for item in page_text['English']['IMPORT_MYTARGET_HINT_ITEMS']:
            assert registration_main_page.text_became_visible(item)

    def test_language_persists_create_cabinet_russian(self, registration_main_page):
        registration_main_page.select_language('Русский')
        registration_main_page.click_create_new_cabinet_button()
        assert registration_main_page.get_selected_language() == 'Русский'

    def test_language_persists_import_mytarget_cabinet_russian(self, registration_main_page):
        registration_main_page.select_language('Русский')
        registration_main_page.click_import_mytarget_cabinet_button()
        assert registration_main_page.get_selected_language() == 'Русский'

    def test_language_persists_create_cabinet_english(self, registration_main_page):
        registration_main_page.select_language('English')
        registration_main_page.click_create_new_cabinet_button()
        assert registration_main_page.get_selected_language() == 'English'

    def test_language_persists_import_mytarget_cabinet_english(self, registration_main_page):
        registration_main_page.select_language('English')
        registration_main_page.click_import_mytarget_cabinet_button()
        assert registration_main_page.get_selected_language() == 'English'
    