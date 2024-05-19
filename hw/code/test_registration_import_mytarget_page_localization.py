from base_case import BaseCase
from ui.locators.registration_import_mytarget_page_locators import page_text

class TestRegistrationImportMytargetPageLocalization(BaseCase):
    def test_import_page_russian(self, registration_import_mytarget_page):
        assert registration_import_mytarget_page.text_became_visible('Русский')
        assert registration_import_mytarget_page.text_became_visible('English')
        registration_import_mytarget_page.select_language('Русский')
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['BACK_BUTTON'])
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['IMPORT_PAGE_TITLE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['IMPORT_PAGE_SUBTITLE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['ADVERTISER_DATIVE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['AGENCY_DATIVE'])
        registration_import_mytarget_page.switch_account_type(page_text['Русский']['ADVERTISER_DATIVE'])
        current_account_type = registration_import_mytarget_page.get_selected_account_switch()
        benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert len(list(benefits)) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[1] == page_text['Русский'][current_account_type][i]['title']
            assert benefit[2] == page_text['Русский'][current_account_type][i]['desc']
        registration_import_mytarget_page.switch_account_type(page_text['Русский']['AGENCY_DATIVE'])
        current_account_type = registration_import_mytarget_page.get_selected_account_switch()
        benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert len(list(benefits)) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[1] == page_text['Русский'][current_account_type][i]['title']
            assert benefit[2] == page_text['Русский'][current_account_type][i]['desc']
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['CONTINUE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['Русский']['CONTINUE_DESC'])

    def test_import_page_english(self, registration_import_mytarget_page):
        assert registration_import_mytarget_page.text_became_visible('Русский')
        assert registration_import_mytarget_page.text_became_visible('English')
        registration_import_mytarget_page.select_language('English')
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['BACK_BUTTON'])
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['IMPORT_PAGE_TITLE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['IMPORT_PAGE_SUBTITLE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['ADVERTISER_DATIVE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['AGENCY_DATIVE'])
        registration_import_mytarget_page.switch_account_type(page_text['English']['ADVERTISER_DATIVE'])
        current_account_type = registration_import_mytarget_page.get_selected_account_switch()
        benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert len(list(benefits)) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[1] == page_text['English'][current_account_type][i]['title']
            assert benefit[2] == page_text['English'][current_account_type][i]['desc']
        registration_import_mytarget_page.switch_account_type(page_text['English']['AGENCY_DATIVE'])
        current_account_type = registration_import_mytarget_page.get_selected_account_switch()
        benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert len(list(benefits)) == 5
        for i, benefit in enumerate(benefits):
            assert benefit[1] == page_text['English'][current_account_type][i]['title']
            assert benefit[2] == page_text['English'][current_account_type][i]['desc']
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['CONTINUE'])
        assert registration_import_mytarget_page.text_became_visible(page_text['English']['CONTINUE_DESC'])
        
    def test_language_persists_back_english(self, registration_import_mytarget_page):
        registration_import_mytarget_page.select_language('English')
        registration_import_mytarget_page.click_back_button()
        assert registration_import_mytarget_page.get_selected_language() == 'English'

    def test_language_persists_back_russian(self, registration_import_mytarget_page):
        registration_import_mytarget_page.select_language('Русский')
        registration_import_mytarget_page.click_back_button()
        assert registration_import_mytarget_page.get_selected_language() == 'Русский'

