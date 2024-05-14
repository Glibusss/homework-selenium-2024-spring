import time
from base_case import BaseCase


class TestStudyingPage(BaseCase):

    def test_studying_modal_opened(self, studying_page):
        studying_page.click_studying_cell()
        assert studying_page.modal_became_visible()
        assert studying_page.modal_header_became_visible()
        assert studying_page.modal_footer_became_visible()
        assert studying_page.modal_content_became_visible()
        assert studying_page.close_button_became_visible()

    def test_studying_modal_closed_by_close_button(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_close_button()
        assert studying_page.modal_became_invisible()

    def test_methods_modal_header_became_visible(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        assert studying_page.method_modal_header_became_visible()
        assert studying_page.method_modal_content_became_visible()
        assert studying_page.close_button_became_visible()
        assert studying_page.close_button_became_visible()

    def test_video_iframe_became_visible(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        studying_page.click_experts_cell()
        assert studying_page.video_iframe_became_visible()

    def test_course_redirect(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        studying_page.click_course_cell()
        studying_page.go_to_new_tab()
        assert self.is_opened('https://expert.vk.com/courses/kak-prodvigat-malyi-biznes-v-vk-reklame')

    def test_tip_became_visible(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        studying_page.click_catalog_with_tips_cell()
        assert studying_page.tips_became_visible()

    def test_stop_onboarding_modal_became_visible(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        studying_page.click_catalog_with_tips_cell()
        studying_page.click_close_tip()
        assert studying_page.stop_onboarding_modal_became_visible()
        assert studying_page.stop_onboarding_modal_buttons_became_visible()
        assert studying_page.stop_onboarding_modal_header_became_visible()   
        assert studying_page.close_button_became_visible()      
       
    def test_stop_onboarding_modal_became_invisible(self, studying_page):
        studying_page.click_studying_cell()
        studying_page.click_catalog_cell()
        studying_page.click_catalog_with_tips_cell()
        studying_page.click_close_tip()
        studying_page.click_cancel_button()
        assert studying_page.stop_onboarding_modal_became_invisible()
        studying_page.click_close_tip()
        studying_page.click_close_button()
        assert studying_page.stop_onboarding_modal_became_invisible()
        studying_page.click_close_tip()
        studying_page.click_break_button()
        assert studying_page.stop_onboarding_modal_became_invisible()
