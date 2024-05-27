from ui.pages.base_page import BasePage
from ui.locators.registration_import_mytarget_page_locators import (
    RegistrationImportMytargetPageLocators,
)


class RegistrationImportMytargetPage(BasePage):
    locators = RegistrationImportMytargetPageLocators()
    url = "https://ads.vk.com/hq/registration/import/target"

    BENEFIT_AMOUNT = 5

    page_text = {
        "Русский": {
            "BACK_BUTTON": "Назад",
            "IMPORT_PAGE_TITLE": "Импорт рекламного кабинета myTarget",
            "IMPORT_PAGE_SUBTITLE": "Далее потребуется войти в рекламный кабинет myTarget и предоставить VK Рекламе доступ к нему:",
            "ACCOUNT_TYPE": "Тип аккаунта",
            "ADVERTISER_DATIVE": "Рекламодателю",
            "AGENCY_DATIVE": "Агентству",
            "advert": [
                {
                    "title": "Настройки аккаунта",
                    "desc": "Будут использованы настройки кабинета и реквизиты",
                },
                {
                    "title": "Мобильные приложения",
                    "desc": "Все мобильные приложения будут привязаны к новому кабинету",
                },
                {
                    "title": "Аудитории",
                    "desc": "Сможете использовать аудитории myTarget в кабинете VK Рекламы",
                },
                {
                    "title": "Кампании",
                    "desc": "Сможете копировать нужные кампании из myTarget в новый кабинет",
                },
                {
                    "title": "Товарные фиды",
                    "desc": "Cможете скопировать нужные товарные фиды в новый кабинет",
                },
            ],
            "agency": [
                {
                    "title": "Клиенты",
                    "desc": "Вы сможете работать с уже созданными клиентами и создавать новых",
                },
                {
                    "title": "Статистика",
                    "desc": "Вся статистика и все отчёты перенесутся из старого кабинета",
                },
                {
                    "title": "Настройки аккаунта",
                    "desc": "Будут использованы настройки кабинета и реквизиты",
                },
                {
                    "title": "Бюджет",
                    "desc": "Перенесётся бюджет из исходного кабинета",
                },
                {
                    "title": "Старый кабинет myTarget",
                    "desc": "Можно будет по-прежнему заходить в свой старый кабинет",
                },
            ],
            "CONTINUE": "Продолжить",
            "CONTINUE_DESC": "На следующем шаге нужно будет войти в кабинет myTarget и дать нужные разрешения VK Рекламе",
        },
        "English": {
            "BACK_BUTTON": "Back",
            "IMPORT_PAGE_TITLE": "Import of myTarget ad account",
            "IMPORT_PAGE_SUBTITLE": "Next, you will need to log in to myTarget account and grant VK Ads access to it:",
            "ACCOUNT_TYPE": "Account type",
            "ADVERTISER_DATIVE": "Advertiser",
            "AGENCY_DATIVE": "Agency",
            "advert": [
                {
                    "title": "Account settings",
                    "desc": "Account settings and details will be used",
                },
                {
                    "title": "Mobile applications",
                    "desc": "All mobile applications will be linked to the new account",
                },
                {
                    "title": "Audiences",
                    "desc": "You will be able to use myTarget audiences in your VK Advertising account",
                },
                {
                    "title": "Campaigns",
                    "desc": "You will be able to copy the necessary campaigns from myTarget to a new account",
                },
                {
                    "title": "Product feeds",
                    "desc": "You will be able to copy the necessary product feeds to the new account",
                },
            ],
            "agency": [
                {
                    "title": "Clients",
                    "desc": "You will be able to work with existing clients and create new ones",
                },
                {
                    "title": "Statistics",
                    "desc": "All statistics and all reports will be transferred from the old account",
                },
                {
                    "title": "Account settings",
                    "desc": "Account settings and details will be used",
                },
                {
                    "title": "Budget",
                    "desc": "The budget from the original office will be transferred",
                },
                {
                    "title": "Old myTarget account",
                    "desc": "You still will be able to log into your old account",
                },
            ],
            "CONTINUE": "Continue",
            "CONTINUE_DESC": "In the next step, you will need to enter the myTarget account and give the necessary permissions to VK Advertising",
        },
    }

    def language_options_became_visible(self) -> bool:
        return self.became_visible(self.locators.TEXT("Русский")) & self.became_visible(
            self.locators.TEXT("English")
        )

    def language_text_became_visible(self, language: str) -> bool:
        benefit_check = self.check_benefit_contents(language, "advert")
        benefit_check &= self.check_benefit_contents(language, "agency")
        return (
            self.became_visible(
                self.locators.TEXT(self.page_text[language]["BACK_BUTTON"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["IMPORT_PAGE_TITLE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["IMPORT_PAGE_SUBTITLE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["ADVERTISER_DATIVE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["AGENCY_DATIVE"])
            )
            & benefit_check
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["CONTINUE"])
            )
            & self.became_visible(
                self.locators.TEXT(self.page_text[language]["CONTINUE_DESC"])
            )
        )

    def check_benefit_contents(self, language: str, account_type: str) -> bool:
        self.switch_account_type_by_value(account_type)
        benefits = self.get_account_type_benefits()
        benefit_check = len(list(benefits)) == self.BENEFIT_AMOUNT
        for i, benefit in enumerate(benefits):
            benefit_check &= benefit[0] is not None
            benefit_check &= (
                benefit[1] == self.page_text[language][account_type][i]["title"]
            )
            benefit_check &= (
                benefit[2] == self.page_text[language][account_type][i]["desc"]
            )
        return benefit_check

    def header_became_visible(self):
        return self.became_visible(self.locators.HEADER)

    def image_became_visible(self):
        return self.became_visible(self.locators.REGISTRATION_IMAGE)

    def click_image(self):
        self.click(self.locators.REGISTRATION_IMAGE)

    def language_switch_became_visible(self):
        return self.became_visible(self.locators.LANGUAGE_SWITCH)

    def get_selected_language(self) -> str:
        return self.find(self.locators.SELECTED_LANGUAGE).text

    def select_language(self, language: str):
        self.click(self.locators.LANGUAGE_BUTTON(language))

    def back_button_became_visible(self):
        return self.became_visible(self.locators.BACK_BUTTON)

    def click_back_button(self):
        self.click(self.locators.BACK_BUTTON)

    def select_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_BUTTON(account_type))

    def account_type_switch_became_visible(self):
        return self.became_visible(self.locators.ACCOUNT_TYPE_SWITCH)

    def get_selected_account_switch(self) -> str:
        return self.find(self.locators.SWITCH_SELECTED_ACCOUNT_TYPE).get_attribute(
            "value"
        )

    def switch_account_type(self, account_type: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_TEXT(account_type))

    def switch_account_type_by_value(self, value: str):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_VALUE(value))

    def switch_account_type_to_advertiser(self):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_VALUE("advert"))

    def switch_account_type_to_agency(self):
        self.scroll_and_click(self.locators.ACCOUNT_TYPE_SELECTOR_BY_VALUE("agency"))

    def get_account_type_benefits(self):
        return list(
            zip(
                self.find_all(self.locators.IMPORT_BENEFIT_ICON),
                [
                    item.text
                    for item in self.find_all(self.locators.IMPORT_BENEFIT_ITEM_TITLE)
                ],
                [
                    item.text
                    for item in self.find_all(self.locators.IMPORT_BENEFIT_ITEM_DESC)
                ],
            )
        )

    def import_continue_button_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_BUTTON)

    def click_import_continue_button(self):
        self.click(self.locators.IMPORT_CONTINUE_BUTTON)

    def import_continue_note_became_visible(self):
        return self.became_visible(self.locators.IMPORT_CONTINUE_DESC)
