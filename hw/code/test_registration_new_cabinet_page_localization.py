from base_case import BaseCase


class TestRegistrationNewCabinetPageLocalization(BaseCase):
    def test_create_page_russian(self, registration_create_cabinet_page):
        assert registration_create_cabinet_page.language_options_became_visible()
        registration_create_cabinet_page.select_language("Русский")
        assert registration_create_cabinet_page.language_text_became_visible("Русский")

    def test_create_page_english(self, registration_create_cabinet_page):
        assert registration_create_cabinet_page.language_options_became_visible()
        registration_create_cabinet_page.select_language("English")
        assert registration_create_cabinet_page.language_text_became_visible("English")

    def test_language_persists_back_english(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.click_back_button()
        assert registration_create_cabinet_page.get_selected_language() == "English"

    def test_language_persists_back_russian(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.click_back_button()
        assert registration_create_cabinet_page.get_selected_language() == "Русский"

    def test_individual_russia_russian_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.select_russia("Русский")
        registration_create_cabinet_page.select_individual_account("Русский")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_fl_vk")

    def test_individual_row_russian_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.select_row_country("Русский")
        registration_create_cabinet_page.select_individual_account("Русский")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_fl_vk")

    def test_individual_russia_english_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_russia("English")
        registration_create_cabinet_page.select_individual_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_fl_vk_en")

    def test_individual_row_english_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_row_country("English")
        registration_create_cabinet_page.select_individual_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_fl_vk_en")

    def test_legal_entity_russia_russian_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.select_russia("Русский")
        registration_create_cabinet_page.select_legal_entity_account("Русский")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_adv_vk")

    def test_legal_entity_russia_english_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_russia("English")
        registration_create_cabinet_page.select_legal_entity_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_adv_vk_en")

    def test_legal_entity_row_russian_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_russia("English")
        registration_create_cabinet_page.select_legal_entity_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_adv_vk")

    def test_legal_entity_row_english_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_row_country("English")
        registration_create_cabinet_page.select_legal_entity_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_adv_vk_en")

    def test_agency_russian_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.select_agency_account("Русский")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_agency_vk")

    def test_agency_english_offer(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.select_agency_account("English")
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("https://ads.vk.com/documents/offer_agency_vk_en")

    def test_ord_russian(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.click_ord_link()
        assert self.is_opened("https://ads.vk.com/documents/ord_clients")

    def test_ord_english(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.click_ord_link()
        assert self.is_opened("https://ads.vk.com/documents/ord_clients")

    def test_tos_russian(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.click_tos_link()
        assert self.is_opened("https://help.mail.ru/legal/terms/adsvk/terms")

    def test_tos_english(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.click_tos_link()
        assert self.is_opened("https://help.mail.ru/legal/terms/adsvk/termsofservice")

    def test_privacy_russian(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("Русский")
        registration_create_cabinet_page.click_privacy_policy_link()
        assert self.is_opened("https://help.mail.ru/legal/terms/adsvk/privacy")

    def test_privacy_english(self, registration_create_cabinet_page):
        registration_create_cabinet_page.select_language("English")
        registration_create_cabinet_page.click_privacy_policy_link()
        assert self.is_opened("https://help.mail.ru/legal/terms/adsvk/euprivacy")
