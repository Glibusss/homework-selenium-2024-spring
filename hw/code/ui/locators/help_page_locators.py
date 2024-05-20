from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class HelpPageLocators(BasePageLocators):
    HELP_CELL = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTypography') and text()='Помощь']",
    )
    HELP_TOOLTIP = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer__')]")
    IFRAME = (By.XPATH, "//iframe")

    @staticmethod
    def TIP_NAME(tip_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiTypography') and text()='{tip_name}']",
        )
