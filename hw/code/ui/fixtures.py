import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.auth_page import AuthPage
from ui.pages.base_page import BasePage
from ui.pages.commerce_page import CommercePage
from ui.pages.registration_main_page import RegistrationMainPage
from ui.pages.registration_create_cabinet_page import RegistrationCreateCabinetPage
from ui.pages.registration_import_mytarget_page import RegistrationImportMytargetPage
from ui.pages.header_before import HeaderBefore
from ui.pages.cabinet_page import CabinetPage
from ui.pages.audience_page import AudiencePage
from ui.pages.budget_page import BudgetPage
from ui.pages.settings_common_page import SettingsCommonPage
from ui.pages.settings_access_page import SettingsAccessPage
from ui.pages.settings_notifications_page import SettingsNotificationsPage
from ui.pages.help_page import HelpPage
from ui.pages.studying_page import StudyingPage
import os
from dotenv import load_dotenv

@pytest.fixture()
def driver(config):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    options = Options()
    if selenoid:
        capabilities = {
            'browserName': 'chrome',
            'version': '118.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://127.0.0.1:4444/wd/hub',
            options=options,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='session')
def credentials_with_cabinet():
    load_dotenv()
    return os.getenv('LOGIN'), os.getenv('PASSWORD')

@pytest.fixture(scope='session')
def credentials_without_cabinet():
    load_dotenv()
    return os.getenv('NEW_LOGIN'), os.getenv('NEW_PASSWORD')

@pytest.fixture
def budget_page(driver, cabinet_page):
    driver.get(BudgetPage.url)
    return BudgetPage(driver=driver)

@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.fixture
def registration_main_page(driver, credentials_without_cabinet, auth_page):
    driver.get(RegistrationMainPage.url)
    auth_page.login_mail_ru(*credentials_without_cabinet)
    return RegistrationMainPage(driver=driver)

@pytest.fixture
def registration_create_cabinet_page(driver, registration_main_page):
    driver.get(RegistrationCreateCabinetPage.url)
    return RegistrationCreateCabinetPage(driver=driver)

@pytest.fixture
def registration_import_mytarget_page(driver, registration_main_page):
    driver.get(RegistrationImportMytargetPage.url)
    return RegistrationImportMytargetPage(driver=driver)

@pytest.fixture
def header_before(driver, credentials_without_cabinet, auth_page):
    driver.get(HeaderBefore.url)
    auth_page.login_mail_ru(*credentials_without_cabinet)
    return HeaderBefore(driver=driver)

@pytest.fixture
def header_after(driver, cabinet_page):
    driver.get(CabinetPage.url)
    auth_page.login_mail_ru(*credentials_with_cabinet)
    return CabinetPage(driver=driver)

@pytest.fixture
def cabinet_page(driver, credentials_with_cabinet, auth_page):
    driver.get(RegistrationMainPage.url)
    auth_page.login_mail_ru(*credentials_with_cabinet)
    return CabinetPage(driver=driver)

@pytest.fixture
def audience_page(driver, cabinet_page):
    driver.get(AudiencePage.url)
    return AudiencePage(driver=driver)

@pytest.fixture
def settings_common_page(driver, cabinet_page):
    driver.get(SettingsCommonPage.url)
    return SettingsCommonPage(driver=driver)

@pytest.fixture
def settings_access_page(driver, cabinet_page):
    driver.get(SettingsAccessPage.url)
    return SettingsAccessPage(driver=driver)

@pytest.fixture
def help_page(driver, cabinet_page):
    return HelpPage(driver=driver)

@pytest.fixture
def studying_page(driver, cabinet_page):
    return StudyingPage(driver=driver)

@pytest.fixture
def settings_notifications_page(driver, cabinet_page):
    driver.get(SettingsNotificationsPage.url)
    return SettingsNotificationsPage(driver=driver)

@pytest.fixture
def commerce_page(driver, cabinet_page):
    driver.get(CommercePage.url)
    return CommercePage(driver=driver)