from selenium.webdriver.common.by import By


class MainPageLocators:

    # button names for this page

    VK_NEWS_BUTTON = "Новости"

    CASES_BUTTON = "Кейсы"

    IDEAS_FORUM_BUTTON = "Форум идей"

    MONETIZATION_BUTTON = "Монетизация"

    HELP_BUTTON = "Справка"

    INSIGHTS_BUTTON = "Полезные материалы"

    EVENTS_BUTTON = "Мероприятия"

    VIDEO_COURSES_BUTTON = "Видеокурсы"

    CERTIFICATION_BUTTON = "Сертификация"

    DOCUMENTS_BUTTON = "Документы"

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
    def NAV_DROPDOWN_MENU_ITEM(text):
        return (
            By.XPATH,
            f"//*[contains(@class, 'SubNavigationItem_content__')]/div/div[text()='{text}']",
        )

    # slides

    CIRCLE_BUTTONS = (
        By.XPATH,
        "//*[contains(@class, 'Bullets_bullet__')]",
    )

    # slides buttons

    FIRST_SLIDE_BUTTON = "Получить бонус"

    SECOND_SLIDE_BUTTON = "Зарегистироваться"

    THIRD_SLIDE_BUTTON = "Зарегистироваться"

    # slide buttons dict

    SLIDES_BUTTONS_LINKS = {
        FIRST_SLIDE_BUTTON: "/promo/firstbonus",
        SECOND_SLIDE_BUTTON: "/hq",
        THIRD_SLIDE_BUTTON: "/hq",
    }

    @staticmethod
    def ACTIVE_SLIDE_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'MainSlider_active__')]/a[contains(@href, '{href}')]",
        )

    # company cases

    GET_ALL_CASES_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'styles_all__') and contains(@href, '/cases')]",
    )

    FIRST_CASE_LINK = "/cases/uvelichivaem-kolichestvo-podpischikov-kejs-hoff"

    SECOND_CASE_LINK = "/cases/prodvigaem-sajt-i-lid-formu-kejs-a101"

    THIRD_CASE_LINK = "/cases/uvelichivaem-okhvat-kejs-gazprombank"

    @staticmethod
    def GET_CASE_ITEM(href):
        return (
            By.XPATH,
            f"//*[contains(@class, 'Case_link__') and contains(@href, '{href}')]",
        )

    # webinars

    WEBINARS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'GetStarted_wrapper__') and contains(@href, '/news/portret-auditorii-sayta-vk-reklama')]",
    )

    # news

    WEBINARS_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'News_wrapper__') and contains(@href, '/events')]",
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
