import pytest
from datetime import datetime
from base_case import BaseCase

CUSTOM_AUDIENCE_NAME = 'Cool Audience'
SOURCE_NAME = 'Ключевые фразы'
KEY_PHRASES = ['buiseness', 'tasks']
class TestAudiencePage(BaseCase):
    def test_create_audience_modal_page_opened(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.create_audience_modal_page_became_visible()
        assert audience_page.audience_name_input_became_visible()
        assert audience_page.sidebar_sign_became_visible()
        assert audience_page.add_source_button_became_visible()
        assert audience_page.footer_buttons_became_visible()
        assert audience_page.cross_button_became_visible()

    def test_create_audience_modal_page_closed(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_cross_button()
        assert audience_page.create_audience_modal_page_became_invisible()
        audience_page.click_create_audience_button()
        audience_page.click_cancel_button()
        assert audience_page.create_audience_modal_page_became_invisible()

    def test_error_long_audience_name(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.enter_audience_name('a' * (audience_page.MAX_LENGTH_OF_AUDIENCE_NAME + 1))
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    def test_add_source_modal_page_became_visible(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_page_became_visible()
        assert audience_page.source_items_became_visible()

    def test_key_phrases_modal_page_became_visible(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        assert audience_page.key_phrases_sidebar_became_visible()
        assert audience_page.key_phrases_textarea_became_visible()
        assert audience_page.minus_key_phrases_textarea_became_visible()
        assert audience_page.period_input_became_visible()

    def test_add_source_by_key_phrases(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        source_card_content = audience_page.get_source_card_content()
        for key_phrase in KEY_PHRASES:
            assert key_phrase in source_card_content

    def test_create_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(SOURCE_NAME)
        audience_page.enter_key_phrases(KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        audience_page.enter_audience_name(CUSTOM_AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert audience_page.get_created_audience_title() == CUSTOM_AUDIENCE_NAME
        audience_page.delete_audience()
        assert audience_page.created_audience_became_invisible()