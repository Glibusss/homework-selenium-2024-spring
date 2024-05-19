import time
from base_case import BaseCase


class TestCommercePage(BaseCase):

    def test_is_commerce_page_opened(self, commerce_page):
        commerce_page.click_create_button()
        assert commerce_page.sidebar_became_visible()
        assert commerce_page.new_catalog_has_h2_content_title()
        assert commerce_page.name_input_became_visible()
        assert commerce_page.has_tabs_content()
        assert commerce_page.sidebar_buttons_became_visible()
        assert commerce_page.cross_button_became_visible()

    def test_is_commerce_page_closed(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_cancel_button()
        assert commerce_page.sidebar_became_invisible()
        commerce_page.click_create_button()
        commerce_page.click_cross_button()
        assert commerce_page.sidebar_became_invisible()

    def test_has_feed_or_community_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()
        assert commerce_page.has_feed_or_community_tabs_content()

    def test_has_input_error_feed_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()

        assert commerce_page.has_input_error_feed_content()

    def test_has_marketplace_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        assert commerce_page.has_marketplace_tabs_content()
        
    def test_has_input_error_marketplace_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        for i in range(0,3):
            assert commerce_page.has_input_error_marketplace_content()

    def test_has_manual_tabs_content(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_manual_tabs()
        assert commerce_page.manual_became_visible()

