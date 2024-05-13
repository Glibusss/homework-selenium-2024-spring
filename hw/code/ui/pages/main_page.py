from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = "https://ads.vk.com/"

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def click_nav_item(self, item_name: str):
        self.click(self.locators.NAV_ITEM(item_name))

    def click_nav_cabinet_button(self):
        self.click(self.locators.NAV_CABINET_BUTTON)

    def open_education_dropdown(self):
        self.hover(self.locators.NAV_ITEM("Обучение"))

    def education_dropdown_contain_items(self, item_names: dict) -> bool:
        for item_name in item_names.keys:
            item = self.find(self.locators.NAV_DROPDOWN_MENU_ITEM(item_name))
            if item is None:
                return False
        return True

    def click_education_dropdown_item(self, item_name: str):
        self.click(self.locators.NAV_DROPDOWN_MENU_ITEM(item_name))

    # slide

    def change_slide(self):
        self.click(self.locators.NONACTIVE_CIRCLE)

    def click_slider_button(self, item_name: str):
        self.click(self.locators.SLIDES_BUTTONS_LINKS[item_name])

    # cases

    def click_see_all(self):
        self.click(self.locators.GET_ALL_CASES_BUTTON)

    def click_case_item(self, item_name: str):
        self.click(self.locators.GET_CASE_ITEM[item_name])

    # webinar

    def click_webinar_item(self):
        self.scroll_and_click(self.locators.WEBINAR_ITEM)

    # news

    # footer

    def click_footer_cabinet_button(self):
        self.scroll_and_click(self.locators.FOOTER_CABINET_BUTTON)

    def click_footer_item(self, item_name: str):
        self.scroll_and_click(self.locators.FOOTER_SECTIONS_ITEM(item_name))
