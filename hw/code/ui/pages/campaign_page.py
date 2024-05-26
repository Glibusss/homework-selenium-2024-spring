from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.campaign_page_locators import CampaignPageLocators


class CampaignPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CampaignPageLocators()

    TARGET_TABS_CONTENT_LIST = ['Сайт', 'Каталог товаров', 'Мобильное приложение', 'Сообщество и профиль', 'Одноклассники', 'Лид-формы и опросы', 'VK Mini Apps и игры', 'Музыка', 'Видео и трансляции', 'Дзен']

    RECOGNITION_TABS_CONTENT_LIST = ['Баннерная реклама', 'Видеореклама', 'Запись ВКонтакте', 'Реклама в Дзене']

    SITE_NAME_INPUT_ERROR_DICT = {'':'Обязательное поле', 'http://nota':'Неверный формат URL', 'https://@#$$.ru':'Неверный формат URL', '.ru':'Неверный формат URL'}

    def name_sign_became_visible(self):
        return self.became_visible(self.locators.NAME_SIGN)

    def has_tabs_title_content(self):
        return self.became_visible(self.locators.TARGET_TABS) and self.became_visible(self.locators.RECOGNITION_TABS)
    
    def has_target_tabs_content_name_sign(self):
        return self.became_visible(self.locators.TARGET_TABS_SIGN)
    
    def has_target_tabs_content_cells(self):
        for t in self.TARGET_TABS_CONTENT_LIST:
            if not self.became_visible(self.locators.CATEGORY_CELL(t)):
                return False
        return True
    
    def has_recognition_tabs_content_name_sign(self):
        return self.became_visible(self.locators.RECOGNITION_TABS_SIGN)
    
    def has_recognition_tabs_content_cells(self):
        for r in self.RECOGNITION_TABS_CONTENT_LIST:
            if not self.became_visible(self.locators.CATEGORY_CELL(r)):
                return False
        return True
    
    def site_name_input_became_visible(self):
        return self.became_visible(self.locators.SITE_NAME_INPUT)
    
    def create_footer_became_visible(self):
        return self.became_visible(self.locators.CREATE_FOOTER)
    
    def has_create_footer_continue_button_content(self):
        return self.became_visible(self.locators.CREATE_FOOTER_CONTINUE)
    
    def has_create_footer_error_button_content(self):
        return self.became_visible(self.locators.CREATE_FOOTER_ERROR)
    
    def click_continue_button(self):
        self.click(self.locators.CREATE_FOOTER_CONTINUE)
    
    def has_error_site_name_content(self):
        for k in self.SITE_NAME_INPUT_ERROR_DICT:
            name = self.find(self.locators.SITE_NAME_INPUT)
            name.clear()
            name.send_keys(k)
            self.click_continue_button()
            if not self.became_visible(self.locators.ERROR_SITE_NAME(self.SITE_NAME_INPUT_ERROR_DICT[k])):
                return False
        return True

    def fill_site_name_with_valid_url(self):
            name = self.find(self.locators.SITE_NAME_INPUT)
            name.clear()
            name.send_keys('https://nota-tabula.ru')

    def banner_became_visible(self):
        return self.became_visible(self.locators.BANNER)
    
    def target_select_became_visible(self):
        return self.became_visible(self.locators.TARGET_ACTION_SELECT)
