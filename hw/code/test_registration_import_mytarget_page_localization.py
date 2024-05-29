from base_case import BaseCase


class TestRegistrationImportMytargetPageLocalization(BaseCase):
    def test_import_page_russian(self, registration_import_mytarget_page):
        assert registration_import_mytarget_page.language_options_became_visible()
        registration_import_mytarget_page.select_language("Русский")
        assert registration_import_mytarget_page.language_text_became_visible("Русский")

    def test_import_page_english(self, registration_import_mytarget_page):
        assert registration_import_mytarget_page.language_options_became_visible()
        registration_import_mytarget_page.select_language("English")
        assert registration_import_mytarget_page.language_text_became_visible("English")

    def test_language_persists_back_english(self, registration_import_mytarget_page):
        registration_import_mytarget_page.select_language("English")
        registration_import_mytarget_page.click_back_button()
        assert registration_import_mytarget_page.get_selected_language() == "English"

    def test_language_persists_back_russian(self, registration_import_mytarget_page):
        registration_import_mytarget_page.select_language("Русский")
        registration_import_mytarget_page.click_back_button()
        assert registration_import_mytarget_page.get_selected_language() == "Русский"

