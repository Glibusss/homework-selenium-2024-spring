import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.upvote_page import UpvotePage


@pytest.fixture()
def driver(config):
    browser = config["browser"]
    url = config["url"]
    selenoid = config["selenoid"]
    vnc = config["vnc"]
    options = Options()
    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "version": "118.0",
        }
        if vnc:
            capabilities["enableVNC"] = True
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub",
            options=options,
            desired_capabilities=capabilities,
        )
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
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


@pytest.fixture
def main_page(driver):
    driver.get(MainPage.url)
    return MainPage(driver=driver)


@pytest.fixture
def upvote_page(driver):
    driver.get(UpvotePage.url)
    return UpvotePage(driver=driver)
