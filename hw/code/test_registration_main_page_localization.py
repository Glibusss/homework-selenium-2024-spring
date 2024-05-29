# from base_case import BaseCase


# class TestRegistrationMainPageLocalization(BaseCase):
#     def test_main_page_russian(self, registration_main_page):
#         assert registration_main_page.language_options_became_visible()
#         registration_main_page.select_language("Русский")
#         assert registration_main_page.language_text_became_visible("Русский")

#     def test_main_page_english(self, registration_main_page):
#         assert registration_main_page.language_options_became_visible()
#         registration_main_page.select_language("English")
#         assert registration_main_page.language_text_became_visible("English")

#     def test_language_persists_create_cabinet_russian(self, registration_main_page):
#         registration_main_page.select_language("Русский")
#         registration_main_page.click_create_new_cabinet_button()
#         assert registration_main_page.get_selected_language() == "Русский"

#     def test_language_persists_import_mytarget_cabinet_russian(
#         self, registration_main_page
#     ):
#         registration_main_page.select_language("Русский")
#         registration_main_page.click_import_mytarget_cabinet_button()
#         assert registration_main_page.get_selected_language() == "Русский"

#     def test_language_persists_create_cabinet_english(self, registration_main_page):
#         registration_main_page.select_language("English")
#         registration_main_page.click_create_new_cabinet_button()
#         assert registration_main_page.get_selected_language() == "English"

#     def test_language_persists_import_mytarget_cabinet_english(
#         self, registration_main_page
#     ):
#         registration_main_page.select_language("English")
#         registration_main_page.click_import_mytarget_cabinet_button()
#         assert registration_main_page.get_selected_language() == "English"

