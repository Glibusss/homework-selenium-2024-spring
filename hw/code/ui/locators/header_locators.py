from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators

class HeaderLocators(BasePageLocators):
    HEADER = (By.TAG_NAME, "HEADER")

    @staticmethod
    def LANGUAGE_BUTTON(language):
        return By.XPATH, f"//*[contains(@class, 'vkuiSegmentedControlOption')]/h4[text()='{language}']"

    SELECTED_LANGUAGE = (By.XPATH, "//*[contains(@class, 'vkuiSegmentedControlOption--checked')]/h4")