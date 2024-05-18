from base_case import BaseCase
from ui.locators.registration_create_cabinet_page_locators import page_text

class TestRegistrationNewCabinetPageLocalization(BaseCase):
    # def test_create_page_russian(self, registration_create_cabinet_page):
    #     assert registration_create_cabinet_page.text_became_visible('Русский')
    #     assert registration_create_cabinet_page.text_became_visible('English')
    #     registration_create_cabinet_page.select_language('Русский')
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['BACK_BUTTON'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['CREATE_PAGE_TITLE'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ACCOUNT_TYPE'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ADVERTISER_NOMINATIVE'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['AGENCY_NOMINATIVE'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['CHOOSE_COUNTRY'])
    #     registration_create_cabinet_page.click_country_selector()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['RUSSIA'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ARMENIA'])
    #     assert registration_create_cabinet_page.image_became_visible()
    #     registration_create_cabinet_page.click_image()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['CURRENCY'])
    #     registration_create_cabinet_page.click_currency_selector()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['RUBLE'])
    #     registration_create_cabinet_page.click_image()
    #     registration_create_cabinet_page.select_country(page_text['Русский']['ARMENIA'])
    #     registration_create_cabinet_page.click_currency_selector()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['DOLLAR'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['EURO'])
    #     registration_create_cabinet_page.click_image()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ROW_INDIVIDUAL_WARNING'])
    #     registration_create_cabinet_page.select_country(page_text['Русский']['RUSSIA'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['INDIVIDUAL'])
    #     registration_create_cabinet_page.hover_account_type_hint(page_text['Русский']['INDIVIDUAL'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['INDIVIDUAL_HINT'])
    #     registration_create_cabinet_page.hover_image()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['LEGAL_ENTITY'])
    #     registration_create_cabinet_page.hover_account_type_hint(page_text['Русский']['LEGAL_ENTITY'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['LEGAL_ENTITY_HINT'])
    #     registration_create_cabinet_page.hover_image()
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['INN'])
    #     # Видно, но не видно
    #     # assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['INN_EXAMPLE'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['FULL_NAME'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ACCEPT_CHECKBOX'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['OFFER'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['ORD'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['TOS'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['PRIVACY'])
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['MAILING'])
    #     registration_create_cabinet_page.hover_mailing_hint('Русский')
    #     assert registration_create_cabinet_page.text_became_visible(page_text['Русский']['MAILING_HINT'])

    def test_create_page_english(self, registration_create_cabinet_page):
        assert registration_create_cabinet_page.text_became_visible('Русский')
        assert registration_create_cabinet_page.text_became_visible('English')
        registration_create_cabinet_page.select_language('English')
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['BACK_BUTTON'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['CREATE_PAGE_TITLE'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ACCOUNT_TYPE'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ADVERTISER_NOMINATIVE'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['AGENCY_NOMINATIVE'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['CHOOSE_COUNTRY'])
        registration_create_cabinet_page.click_country_selector()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['RUSSIA'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ARMENIA'])
        assert registration_create_cabinet_page.image_became_visible()
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['CURRENCY'])
        registration_create_cabinet_page.click_currency_selector()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['RUBLE'])
        registration_create_cabinet_page.click_image()
        registration_create_cabinet_page.select_country(page_text['English']['ARMENIA'])
        registration_create_cabinet_page.click_currency_selector()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['DOLLAR'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['EURO'])
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ROW_INDIVIDUAL_WARNING'])
        registration_create_cabinet_page.select_country(page_text['English']['RUSSIA'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['INDIVIDUAL'])
        registration_create_cabinet_page.hover_account_type_hint(page_text['English']['INDIVIDUAL'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['INDIVIDUAL_HINT'])
        registration_create_cabinet_page.hover_image()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['LEGAL_ENTITY'])
        registration_create_cabinet_page.hover_account_type_hint(page_text['English']['LEGAL_ENTITY'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['LEGAL_ENTITY_HINT'])
        registration_create_cabinet_page.hover_image()
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['INN'])
        # Видно, но не видно
        # assert registration_create_cabinet_page.text_became_visible(page_text['English']['INN_EXAMPLE'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['FULL_NAME'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ACCEPT_CHECKBOX'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['OFFER'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['ORD'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['TOS'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['PRIVACY'])
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['MAILING'])
        registration_create_cabinet_page.hover_mailing_hint('English')
        assert registration_create_cabinet_page.text_became_visible(page_text['English']['MAILING_HINT'])

    # def test_language_persists_back_english(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.click_back_button()
    #     assert registration_create_cabinet_page.get_selected_language() == 'English'

    # def test_language_persists_back_russian(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.click_back_button()
    #     assert registration_create_cabinet_page.get_selected_language() == 'Русский'

    # def test_individual_russia_russian_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.select_country(page_text['Русский']['RUSSIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['Русский']['INDIVIDUAL'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_fl_vk')

    # def test_individual_row_russian_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.select_country(page_text['Русский']['ARMENIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['Русский']['INDIVIDUAL'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_fl_vk')

    # def test_individual_russia_english_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.select_country(page_text['English']['RUSSIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['English']['INDIVIDUAL'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_fl_vk_en')

    # def test_individual_row_english_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.select_country(page_text['English']['ARMENIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['English']['INDIVIDUAL'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_fl_vk_en')

    # def test_legal_entity_russia_russian_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.select_country(page_text['Русский']['RUSSIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['Русский']['LEGAL_ENTITY'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_adv_vk')

    # def test_legal_entity_russia_english_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.select_country(page_text['English']['RUSSIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['English']['LEGAL_ENTITY'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_adv_vk_en')

    # def test_legal_entity_row_russian_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.select_country(page_text['Русский']['ARMENIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['Русский']['LEGAL_ENTITY'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_adv_vk')

    # def test_legal_entity_row_english_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.select_country(page_text['English']['ARMENIA'])
    #     registration_create_cabinet_page.select_account_type(page_text['English']['LEGAL_ENTITY'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_adv_vk_en')

    # def test_agency_russian_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.select_account_type(page_text['Русский']['AGENCY_NOMINATIVE'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_agency_vk')

    # def test_agency_english_offer(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.select_account_type(page_text['English']['AGENCY_NOMINATIVE'])
    #     registration_create_cabinet_page.click_offer_link()
    #     assert self.is_opened('https://ads.vk.com/documents/offer_agency_vk_en')

    # def test_ord_russian(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.click_ord_link()
    #     assert self.is_opened('https://ads.vk.com/documents/ord_clients')

    # def test_ord_english(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.click_ord_link()
    #     assert self.is_opened('https://ads.vk.com/documents/ord_clients')

    # def test_tos_russian(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.click_tos_link()
    #     assert self.is_opened('https://help.mail.ru/legal/terms/adsvk/terms')

    # def test_tos_english(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.click_tos_link()
    #     assert self.is_opened('https://help.mail.ru/legal/terms/adsvk/termsofservice')

    # def test_privacy_russian(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('Русский')
    #     registration_create_cabinet_page.click_privacy_policy_link()
    #     assert self.is_opened('https://help.mail.ru/legal/terms/adsvk/privacy')

    # def test_privacy_english(self, registration_create_cabinet_page):
    #     registration_create_cabinet_page.select_language('English')
    #     registration_create_cabinet_page.click_privacy_policy_link()
    #     assert self.is_opened('https://help.mail.ru/legal/terms/adsvk/euprivacy')