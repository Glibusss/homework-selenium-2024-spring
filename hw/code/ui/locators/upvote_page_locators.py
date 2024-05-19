from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class UpvotePageLocators(BasePageLocators):
    IDEAS_SEARCH_INPUT = (
        By.XPATH,
        "//*[contains(@class, 'vkuiSearch__input') and contains(@placeholder, 'Поиск по ID или заголовку')]",
    )

    IDEAS_THEME_FILTER_BUTTON = (
        By.XPATH,
        "//span[contains(@class, 'vkuiSelect__title') and text()='Любая тема']",
    )

    STATUS_FILTER_BUTTON = (
        By.XPATH,
        "//span[contains(@class, 'vkuiSelect__title') and text()='Любой статус']",
    )

    CANCEL_FILTER_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiIcon--cancel')]",
    )

    ADD_IDEA_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Предложить идею']",
    )

    CLOSE_IDEA_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__content') and text()='Ок, понятно']",
    )

    IDEA_CARD = (By.XPATH, "//*[contains(@class, 'Idea_cardVote__')]")

    IDEA_TITLE = (By.XPATH, "//*[contains(@class, 'Idea_title__')]")

    IDEA_DATE_AND_ID = (By.XPATH, "//*[contains(@class, 'vkuiSimpleCell__text')]")

    IDEA_THEME = (
        By.XPATH,
        "//*[contains(@class, 'Tag_tag__')]//*[contains(@class, 'vkuiText')]",
    )

    IDEA_THEME_CLASSNAME_IN_CARD = "vkuiText"

    IDEA_STATUS = (
        By.XPATH,
        "//*[contains(@class, 'Status_wrap__')]//*[contains(@class, 'Status_text__')]",
    )

    IDEA_COMMENTS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'ButtonComment_button__')]//*[contains(@class, 'vkuiButton__content')]",
    )

    @staticmethod
    def DROPDOWN_MENU_ITEM(item_name):
        return (
            By.XPATH,
            f"//*[contains(@class, 'vkuiCustomSelectDropdown')]//*[text()='{item_name}']",
        )

    COMMENT_CELL = (
        By.XPATH,
        "//*[contains(@class, 'Comment_commentsWrap__')]//*[contains(@class, 'Comment_cell__')]",
    )

    IDEA_LINK = (
        By.XPATH,
        "//*[contains(@class, 'Idea_title__')]",
    )

    LINK_COPY_BUTTON = (By.XPATH, "//*[contains(@class, 'Idea_copyLinkBtn__')]")
    