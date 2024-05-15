import time
from base_case import BaseCase


class TestCommercePage(BaseCase):
    ERRORS_FEED_LIST = ['Необходимо указать протокол http(s)', 'Невалидный url', 'Неверный формат файла', 'Не удалось выполнить запрос по HTTP']
    INPUTS_FEED_LIST = ['h', 'http://', 'https://nota-tabula.ru', 'https://nota-tabula.rur']

    ERRORS_MARKETPLACE_LIST = ['Необходимо указать протокол http(s)', 'Невалидный url', 'Введите корректную ссылку на страницу продавца на поддерживаемом маркетпласе']
    INPUTS_MARKETPLACE_LIST = ['h', 'http://', 'https://www.wildberries.rus/brands/310451382-miryuyu']

    def test_is_commerce_page_opened(self, commerce_page):
        commerce_page.click_create_button()
        assert commerce_page.sidebar_became_visible()
        assert commerce_page.new_catalog_h2_became_visible()
        assert commerce_page.name_input_became_visible()
        assert commerce_page.tabs_became_visible()
        assert commerce_page.sidebar_buttons_became_visible()
        assert commerce_page.cross_button_became_visible()

    def test_is_commerce_page_closed(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_cancel_button()
        assert commerce_page.sidebar_became_invisible()
        commerce_page.click_create_button()
        commerce_page.click_cross_button()
        assert commerce_page.sidebar_became_invisible()

    def test_is_feed_or_community_became_visible(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()
        assert commerce_page.feed_or_community_became_visible()

    def test_is_feed_errors_become_visible(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_feed_tabs()

        for i in range(0,4):
            assert commerce_page.input_error_feed_became_visible(self.INPUTS_FEED_LIST[i], self.ERRORS_FEED_LIST[i])

    def test_is_marketplace_became_visible(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        assert commerce_page.marketplace_became_visible()
        
    def test_is_marketplace_errors_become_visible(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_marketplace_tabs()
        for i in range(0,3):
            assert commerce_page.input_error_marketplace_became_visible(self.INPUTS_MARKETPLACE_LIST[i], self.ERRORS_MARKETPLACE_LIST[i])

    def test_is_manual_tabs_became_visible(self, commerce_page):
        commerce_page.click_create_button()
        commerce_page.click_manual_tabs()
        assert commerce_page.manual_became_visible()
