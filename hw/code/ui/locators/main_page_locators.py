from selenium.webdriver.common.by import By


class MainPageLocators:

    # button names for this page

    VK_NEWS_BUTTON = "Новости"

    CASES_BUTTON = "Кейсы"

    IDEAS_FORUM_BUTTON = "Форум идей"

    MONETIZATION_BUTTON = "Монетизация"

    INFORMATION_BUTTON = "Справка"

    HELP_BUTTON = "Помощь"

    INSIGHTS_BUTTON = "Полезные материалы"

    EVENTS_BUTTON = "Мероприятия"

    VIDEO_COURSES_BUTTON = "Видеокурсы"

    CERTIFICATION_BUTTON = "Сертификация"

    DOCUMENTS_BUTTON = "Документы"

    EDUCATION_FOR_BUSINESS = "Обучение для бизнеса"

    # main page links dict

    MAIN_PAGE_LINKS = {
        VK_NEWS_BUTTON: "/news",
        CASES_BUTTON: "/cases",
        IDEAS_FORUM_BUTTON: "/upvote",
        MONETIZATION_BUTTON: "/partner",
        INSIGHTS_BUTTON: "/insights",
        EVENTS_BUTTON: "/events",
        VIDEO_COURSES_BUTTON: "https://expert.vk.com/catalog/courses/",
        CERTIFICATION_BUTTON: "https://expert.vk.com/certification/",
        DOCUMENTS_BUTTON: "/documents",
        EDUCATION_FOR_BUSINESS: "https://expert.vk.com/",
        INFORMATION_BUTTON: "/help",
        HELP_BUTTON: "/help",
    }

    # unique buttons in header

    VK_ADS_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home__')]")

    NAV_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAds_right__')]/a[contains(@class, 'ButtonCabinet_primary__')]",
    )

    @staticmethod
    def NAV_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'NavigationVKAdsItem_link__') and contains(@href, '{href}')]",
        )

    # dropdown menu button

    NAV_EDUCATION_DROPDOWN_MENU_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'NavigationVKAdsItem_item__') and text()='Обучение']",
    )

    @staticmethod
    def NAV_DROPDOWN_MENU_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'SubNavigationItem_content__') and contains(@href, '{href}')]",
        )

    # company cases

    GET_ALL_CASES_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'styles_all__') and contains(@href, '/cases')]",
    )

    CASE_LINK = (
        By.XPATH,
        "//*[contains(@class, 'Case_link__')]",
    )

    CASE_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Case_title__')]",
    )

    CASE_NEW_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Summary_title__')]",
    )

    # webinars

    WEBINARS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'GetStarted_button__')]",
    )

    # news

    NEWS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'News_button__')]",
    )

    # footer buttons

    FOOTER_CABINET_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'Footer_leftContent__')]/a[contains(@class, 'ButtonCabinet_primary__')]",
    )

    @staticmethod
    def FOOTER_SECTIONS_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'Footer_item__')]/a[contains(@href, '{href}')]",
        )
