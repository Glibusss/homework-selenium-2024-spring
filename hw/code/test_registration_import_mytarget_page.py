from base_case import BaseCase


class TestRegistrationImportMytargetPage(BaseCase):
    def test_import_page_rendering(self, registration_import_mytarget_page):
        current_language = registration_import_mytarget_page.get_selected_language()
        current_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        assert registration_import_mytarget_page.header_became_visible()
        assert registration_import_mytarget_page.image_became_visible()
        assert registration_import_mytarget_page.language_switch_became_visible()
        assert registration_import_mytarget_page.back_button_became_visible()
        assert registration_import_mytarget_page.account_type_switch_became_visible()
        assert registration_import_mytarget_page.check_benefit_contents(
            current_language, current_account_type
        )
        assert registration_import_mytarget_page.import_continue_button_became_visible()
        assert registration_import_mytarget_page.import_continue_note_became_visible()

    def test_import_page_back_button(self, registration_import_mytarget_page):
        registration_import_mytarget_page.click_back_button()
        assert self.is_opened("https://ads.vk.com/hq/registration")

    def test_import_page_account_switch_to_agency(
        self, registration_import_mytarget_page
    ):
        current_language = registration_import_mytarget_page.get_selected_language()
        registration_import_mytarget_page.switch_account_type_to_agency()
        current_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        assert registration_import_mytarget_page.check_benefit_contents(
            current_language, current_account_type
        )

    def test_import_page_account_switch_to_advertiser(
        self, registration_import_mytarget_page
    ):
        current_language = registration_import_mytarget_page.get_selected_language()
        current_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        registration_import_mytarget_page.switch_account_type_to_agency()
        registration_import_mytarget_page.switch_account_type_to_advertiser()
        new_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        assert current_account_type == new_account_type
        assert registration_import_mytarget_page.check_benefit_contents(
            current_language, current_account_type
        )

    def test_import_page_switch_same_advertiser(
        self, registration_import_mytarget_page
    ):
        current_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        current_benefits = registration_import_mytarget_page.get_account_type_benefits()
        registration_import_mytarget_page.switch_account_type_by_value(
            current_account_type
        )
        new_benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert current_benefits == new_benefits

    def test_import_page_switch_same_agency(self, registration_import_mytarget_page):
        registration_import_mytarget_page.switch_account_type_to_agency()
        current_account_type = (
            registration_import_mytarget_page.get_selected_account_switch()
        )
        current_benefits = registration_import_mytarget_page.get_account_type_benefits()
        registration_import_mytarget_page.switch_account_type_by_value(
            current_account_type
        )
        new_benefits = registration_import_mytarget_page.get_account_type_benefits()
        assert current_benefits == new_benefits

    def test_continue_import(self, registration_import_mytarget_page):
        registration_import_mytarget_page.click_import_continue_button()
        assert self.is_opened(url="target.my.com")
        