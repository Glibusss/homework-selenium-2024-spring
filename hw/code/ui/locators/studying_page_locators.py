from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class StudyingPageLocators(BasePageLocators):
    STUDY_CELL = (By.XPATH, "//*[text()='Обучение']")

    CHOOSE_STUDYING_MODAL = (By.XPATH, "//*[contains(@class, 'vkuiModalPage')]")
    MODAL_OVERLAY = (By.XPATH, "//*[contains(@class, 'ModalRoot_overlay__')]")

    STUDYING_MODAL_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-2') and text()='С чего начнём обучение?']",
    )
    STUDYING_MODAL_H4 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiHeadline--level-2') and text()='Выберите, что будете рекламировать']",
    )

    @staticmethod
    def SOURCE_ITEM(item_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiTypography') and text()='{item_name}']",
        )

    STUDYING_MODAL_FOOTER_SIGN = (By.XPATH, "//*[contains(@class, 'vkuiFootnote')]")
    LATER_BUTTON = (By.XPATH, "//*[contains(@class, 'Objects_closeModalButton__')]")

    CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")

    STUDYING_METHOD_MODAL_H2 = (
        By.XPATH,
        "//*[contains(@class, 'vkuiTitle--level-2') and text()='Как хотите учиться?']",
    )

    IFRAME = (By.XPATH, "//iframe[contains(@class, 'VideoOnboardingModal_frame__')]")

    TIP = (By.XPATH, "//*[contains(@class, 'PopoverContent_root__')]")
    SIDEBAR = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_')]")
    TIP_CLOSE = (By.XPATH, "//*[contains(@class, 'RichTooltop_closeBtn__')]")

    TIP_CLOSE_MODAL_H2 = (
        By.XPATH,
        "//h2[contains(@class, 'vkuiTitle--level-2') and text()='Прервать обучение?']",
    )
    TIP_CLOSE_MODAL_H4 = (
        By.XPATH,
        "//h5[text()='Вернуться к обучению можно когда угодно']",
    )

    # Напрямую через спан не работает
    CANCEL_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'StopOnboardingModal_content__')]//span[contains(@class, 'vkuiButton__content') and text()='Отмена']",
    )
    BREAK_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Прервать']",
    )

    STOP_ONBOARDING_MODAL = (
        By.XPATH,
        "//*[contains(@class, 'StopOnboardingModal_content__')]",
    )

