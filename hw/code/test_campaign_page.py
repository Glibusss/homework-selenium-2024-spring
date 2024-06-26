import time
from base_case import BaseCase


class TestCampaignPage(BaseCase):

    def test_campaign_group_ad_created(self, campaign_page):
        campaign_page.click_create_button()
        assert campaign_page.name_sign_became_visible()
        assert campaign_page.has_tabs_title_content()
        assert campaign_page.has_target_tabs_content_name_sign()
        assert campaign_page.has_target_tabs_content_cells()
        campaign_page.click_recognition_tabs()
        assert campaign_page.has_recognition_tabs_content_name_sign()
        assert campaign_page.has_recognition_tabs_content_cells()
        campaign_page.click_target_tabs()
        campaign_page.click_site_cell()
        assert campaign_page.site_name_input_became_visible()
        campaign_page.fill_site_name_with_valid_url()
        campaign_page.click_target_tabs()
        assert campaign_page.banner_became_visible()
        assert campaign_page.target_select_became_visible()
        assert campaign_page.switch_became_visible()
        assert campaign_page.strategy_action_select_became_visible()
        assert campaign_page.budget_inputs_became_visible()
        assert campaign_page.data_inputs_became_visible()
        assert campaign_page.create_footer_became_visible()
        assert campaign_page.has_create_footer_continue_button_content()
        campaign_page.rename_entity(campaign_page.CAMPAIGN_NAME)
        campaign_page.fill_campaign_form()
        campaign_page.click_continue_button()

        assert self.is_opened(r"https://ads\.vk\.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_\d+")
        assert campaign_page.name_sign_became_visible()
        campaign_page.rename_entity(campaign_page.GROUP_NAME)
        assert campaign_page.has_sections_title_content()
        assert campaign_page.has_section_region_region_buttons_content()
        campaign_page.click_russia_button()
        campaign_page.click_demography_section()
        assert campaign_page.has_age_select_content()
        assert campaign_page.has_pegi_select_content()
        campaign_page.fill_demography()
        campaign_page.click_demography_section()
        campaign_page.click_interest_section()
        assert campaign_page.interest_subsection_became_visible()
        campaign_page.click_interest_subsection()
        assert campaign_page.has_interest_subsection_content()
        campaign_page.fill_interests()
        campaign_page.click_stop_interest_opener()
        campaign_page.has_stop_interest_content()
        campaign_page.fill_stop_interest()
        campaign_page.click_interest_section()
        campaign_page.click_device_section()
        assert campaign_page.has_device_section_content()
        campaign_page.click_mobile_checkbox()
        campaign_page.click_continue_button()

        assert self.is_opened(r"https://ads\.vk\.com/hq/new_create/ad_plan/new-site_conversions/ad_group/new-ad-group-form_\d+/ad/new-ad-form_\d+")
        assert campaign_page.name_sign_became_visible()
        assert campaign_page.logo_input_became_visible()
        assert campaign_page.has_ads_inputs_content()
        assert campaign_page.has_ads_textarea_content()
        assert campaign_page.mediatec_became_visible()
        campaign_page.rename_entity(campaign_page.AD_NAME)
        campaign_page.click_logo_input()
        assert campaign_page.has_media_sidebar_content()
        campaign_page.click_image_item()
        assert campaign_page.preview_image_became_visible()
        campaign_page.fill_ad_inputs_and_textarea()
        campaign_page.click_media()
        campaign_page.has_mediatec_sidebar_image_content()
        campaign_page.click_image_item()
        campaign_page.submit_button_became_visible()
        campaign_page.click_submit_button()
        assert campaign_page.media_content_list_became_visible()
        assert campaign_page.buttons_changed()
        #ГРУЗЯТСЯ ИЗОБРАЖЕНИЯ. БОЛЬШЕ НИКАК
        time.sleep(10)
        campaign_page.click_publish_button()
        assert campaign_page.has_bug_modal_content()
        campaign_page.click_send_bug_modal()

        assert self.is_opened('https://ads.vk.com/hq/dashboard/ad_plans')
        assert campaign_page.has_campaign_page_tabs_content()
        assert campaign_page.action_select_became_visible()
        assert campaign_page.checkbox_all_became_visible()
        assert campaign_page.check_campaign_title()
        assert campaign_page.check_campaign_budget()
        assert campaign_page.check_campaign_action()
        campaign_page.hover_campaign_title()
        assert campaign_page.edit_became_visible()
        campaign_page.click_edit()
        assert campaign_page.check_title_input_value_campaign()
        assert campaign_page.check_site_name_value_campaign()
        assert campaign_page.check_action_select_value_campaign()
        assert campaign_page.check_strategy_select_value_campaign()
        assert campaign_page.check_budget_input_value_campaign()
        assert campaign_page.check_budget_period_input_value_campaign()
        campaign_page.click_cancel_button()

        campaign_page.click_group_tabs()
        assert campaign_page.check_group_title()
        assert campaign_page.action_select_became_visible()
        assert campaign_page.checkbox_all_became_visible()
        campaign_page.hover_group_title()
        assert campaign_page.edit_became_visible()
        campaign_page.click_edit()
        assert campaign_page.check_title_input_value_group()
        assert campaign_page.check_selected_region()
        assert campaign_page.check_ages()
        assert campaign_page.check_pegi()
        assert campaign_page.check_interest()
        assert campaign_page.check_stop_interest()
        assert campaign_page.check_devices()
        campaign_page.click_cancel_button()

        campaign_page.click_ad_tab()
        assert campaign_page.check_ad_title()
        assert campaign_page.action_select_became_visible()
        assert campaign_page.checkbox_all_became_visible()
        campaign_page.hover_ad_title()
        assert campaign_page.edit_became_visible()
        campaign_page.click_edit()
        assert campaign_page.preview_image_became_visible()
        assert campaign_page.media_content_list_became_visible()
        assert campaign_page.check_ad_name()
        assert campaign_page.check_ad_short_description()
        assert campaign_page.check_ad_long_description()
        assert campaign_page.check_ad_button_text()
        assert campaign_page.check_ad_advertiser()
        campaign_page.click_cancel_button()

        campaign_page.delete_entity()

