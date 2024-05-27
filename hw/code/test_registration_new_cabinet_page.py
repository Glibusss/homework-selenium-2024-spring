import pytest
import time
from selenium.common.exceptions import TimeoutException
from base_case import BaseCase


class TestRegistrationNewCabinetPage(BaseCase):
    def test_create_page_rendering(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        assert registration_create_cabinet_page.header_became_visible()
        assert registration_create_cabinet_page.image_became_visible()
        assert registration_create_cabinet_page.language_switch_became_visible()
        assert registration_create_cabinet_page.back_button_became_visible()
        assert registration_create_cabinet_page.create_page_title_became_visible()
        assert registration_create_cabinet_page.account_type_label_became_visible(
            current_language
        )
        assert registration_create_cabinet_page.account_type_buttons_became_visible()
        assert registration_create_cabinet_page.country_selector_became_visible()
        assert registration_create_cabinet_page.currency_selector_became_visible()
        assert registration_create_cabinet_page.email_input_became_visible()
        assert registration_create_cabinet_page.entity_type_buttons_became_visible()
        assert registration_create_cabinet_page.inn_input_became_visible()
        assert registration_create_cabinet_page.name_input_became_visible()
        assert registration_create_cabinet_page.offer_checkbox_became_visible()
        assert registration_create_cabinet_page.offer_link_became_visible()
        assert registration_create_cabinet_page.ord_link_became_visible()
        assert registration_create_cabinet_page.tos_link_became_visible()
        assert registration_create_cabinet_page.privacy_policy_link_became_visible()
        assert registration_create_cabinet_page.mailing_checkbox_became_visible(
            current_language
        )
        assert registration_create_cabinet_page.mailing_hint_became_visible(
            current_language
        )
        assert registration_create_cabinet_page.create_cabinet_button_became_visible()

    def test_create_page_back_button(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_back_button()
        assert self.is_opened("https://ads.vk.com/hq/registration")

    def test_country_dropdown(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_country_selector()
        assert registration_create_cabinet_page.country_list_became_visible()

    def test_currency_dropdown(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_currency_selector()
        assert registration_create_cabinet_page.currency_list_became_visible()

    def test_russia_currencies(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_russia(current_language)
        assert registration_create_cabinet_page.check_russia_currency_options(
            current_language
        )

    def test_row_currencies(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_row_country(current_language)
        assert registration_create_cabinet_page.check_row_currency_options(
            current_language
        )

    def test_correct_email_1(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test@email.com")
        with pytest.raises(TimeoutException):
            registration_create_cabinet_page.click_image()
            registration_create_cabinet_page.get_email_error(timeout=3)

    def test_correct_email_2(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("A@b.co")
        with pytest.raises(TimeoutException):
            registration_create_cabinet_page.click_image()
            registration_create_cabinet_page.get_email_error(timeout=3)

    def test_incorrect_email_1(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_email_error()

    def test_incorrect_email_2(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("123")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_email_error()

    def test_incorrect_email_3(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test@.com")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_email_error()

    def test_reenter_correct_email(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test@.com")
        registration_create_cabinet_page.click_image()
        registration_create_cabinet_page.enter_email("test@email.com")
        with pytest.raises(TimeoutException):
            registration_create_cabinet_page.click_image()
            registration_create_cabinet_page.get_email_error(timeout=3)

    def test_empty_email(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test@.com")
        registration_create_cabinet_page.click_image()
        registration_create_cabinet_page.enter_email("")
        assert registration_create_cabinet_page.get_email_error()

    def test_advertiser_entity_types(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_advertiser_account(current_language)
        assert (
            registration_create_cabinet_page.entity_type_button_count()
            == registration_create_cabinet_page.ADVERTISER_ENTITY_TYPE_COUNT
        )

    def test_agency_entity_types(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_agency_account(current_language)
        # Перерендер занимает какое-то время, без слипа список кнопок не успевает обновиться
        time.sleep(1)
        assert (
            registration_create_cabinet_page.entity_type_button_count()
            == registration_create_cabinet_page.AGENCY_ENTITY_TYPE_COUNT
        )

    def test_individual_inputs(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_legal_entity_account(current_language)
        registration_create_cabinet_page.select_individual_account(current_language)
        assert registration_create_cabinet_page.inn_input_became_visible()
        assert registration_create_cabinet_page.name_input_became_visible()

    def test_row_individual_entity(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_row_country(current_language)
        registration_create_cabinet_page.select_individual_account(current_language)
        assert registration_create_cabinet_page.row_individual_warning_became_visible()
        assert registration_create_cabinet_page.inn_input_became_visible()

    def test_create_page_individual_hint(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        assert registration_create_cabinet_page.check_individual_hint_content(
            current_language
        )

    def test_correct_inn(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.enter_inn("123456789012")
        registration_create_cabinet_page.click_image()
        with pytest.raises(TimeoutException):
            registration_create_cabinet_page.get_inn_error(current_language, timeout=3)

    def test_incorrect_inn(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.enter_inn("1")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_inn_error(current_language)

    def test_reenter_correct_inn(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.enter_inn("1")
        registration_create_cabinet_page.click_image()
        registration_create_cabinet_page.enter_inn("123456789012")
        registration_create_cabinet_page.click_image()
        with pytest.raises(TimeoutException):
            registration_create_cabinet_page.get_inn_error(current_language, timeout=3)

    def test_numbers_in_inn(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_inn("123")
        assert registration_create_cabinet_page.get_entered_inn() == "123"

    def test_cyrillic_in_inn(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_inn("тест")
        assert registration_create_cabinet_page.get_entered_inn() == ""

    def test_latin_in_inn(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_inn("test")
        assert registration_create_cabinet_page.get_entered_inn() == ""

    def test_inn_bug(self, registration_create_cabinet_page, registration_main_page):
        registration_create_cabinet_page.enter_name("Test")
        registration_create_cabinet_page.click_currency_selector()
        registration_create_cabinet_page.click_back_button()
        registration_main_page.click_create_new_cabinet_button()
        assert registration_create_cabinet_page.get_entered_inn() == "Test"

    def test_10_char_inn(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.enter_inn("1234567890")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_inn_error(current_language)

    def test_14_char_inn(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.enter_inn("12345678901234")
        registration_create_cabinet_page.click_image()
        assert registration_create_cabinet_page.get_inn_error(current_language)

    def test_legal_entity_no_inputs(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_legal_entity_account(current_language)
        assert not registration_create_cabinet_page.inn_input_became_visible()
        assert not registration_create_cabinet_page.name_input_became_visible()

    def test_create_page_legal_entity_hint(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        assert registration_create_cabinet_page.check_legal_entity_hint_content(
            current_language
        )

    def test_uncheck_offer_checkbox(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.click_offer_checkbox()
        assert registration_create_cabinet_page.offer_checkbox_unchecked(
            current_language
        )

    def test_check_offer_checkbox(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.click_offer_checkbox()
        registration_create_cabinet_page.click_offer_checkbox()
        assert registration_create_cabinet_page.offer_checkbox_checked(current_language)

    def test_individual_russia_offer(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_russia(current_language)
        registration_create_cabinet_page.select_individual_account(current_language)
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("ads.vk.com/documents/offer_fl_vk")

    def test_individual_row_offer(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_row_country(current_language)
        registration_create_cabinet_page.select_individual_account(current_language)
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("ads.vk.com/documents/offer_fl_vk")

    def test_legal_entity_russia_offer(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_russia(current_language)
        registration_create_cabinet_page.select_legal_entity_account(current_language)
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("ads.vk.com/documents/offer_adv_vk")

    def test_legal_entity_row_offer(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_row_country(current_language)
        registration_create_cabinet_page.select_legal_entity_account(current_language)
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("ads.vk.com/documents/offer_adv_vk")

    def test_agency_offer(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.select_agency_account(current_language)
        registration_create_cabinet_page.click_offer_link()
        assert self.is_opened("ads.vk.com/documents/offer_agency_vk")

    def test_ord(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_ord_link()
        assert self.is_opened("ads.vk.com/documents/ord_clients")

    def test_tos(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_tos_link()
        assert self.is_opened("help.mail.ru/legal/terms/adsvk/terms")

    def test_privacy_policy(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_privacy_policy_link()
        assert self.is_opened("help.mail.ru/legal/terms/adsvk/privacy")

    def test_uncheck_mailing_checkbox(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.click_mailing_checkbox(current_language)
        assert registration_create_cabinet_page.mailing_checkbox_unchecked(
            current_language
        )

    def test_check_mailing_checkbox(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.click_mailing_checkbox(current_language)
        registration_create_cabinet_page.click_mailing_checkbox(current_language)
        assert registration_create_cabinet_page.mailing_checkbox_checked(
            current_language
        )

    def test_mailing_hint(self, registration_create_cabinet_page):
        current_language = registration_create_cabinet_page.get_selected_language()
        registration_create_cabinet_page.hover_mailing_hint(current_language)
        assert registration_create_cabinet_page.mailing_hint_window_became_visible()

    def test_advertiser_individual_empty_email(self, registration_create_cabinet_page):
        registration_create_cabinet_page.click_create_cabinet_button()
        assert registration_create_cabinet_page.get_email_error()

    def test_advertiser_individual_wrong_email(self, registration_create_cabinet_page):
        registration_create_cabinet_page.enter_email("test")
        registration_create_cabinet_page.click_create_cabinet_button()
        assert registration_create_cabinet_page.get_email_error()

    def test_advertiser_individual_empty_email_no_agree(
        self, registration_create_cabinet_page
    ):
        registration_create_cabinet_page.click_offer_checkbox()
        registration_create_cabinet_page.click_create_cabinet_button()
        assert registration_create_cabinet_page.get_email_error()
        assert registration_create_cabinet_page.get_offer_error()

    def test_advertiser_individual_wrong_email_no_agree(
        self, registration_create_cabinet_page
    ):
        registration_create_cabinet_page.enter_email("test")
        current_language = registration_create_cabinet_page.get_selected_language()
        # Клик по странице при вводе в текстовое поле вызывает проверку и останавливает обработку события, надо кликнуть ещё раз
        while not registration_create_cabinet_page.offer_checkbox_unchecked(
            current_language
        ):
            registration_create_cabinet_page.click_offer_checkbox()
        registration_create_cabinet_page.click_create_cabinet_button()
        assert registration_create_cabinet_page.get_email_error()
        assert registration_create_cabinet_page.get_offer_error()
