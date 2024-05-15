import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    url = "https://ads.vk.com/"

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 7
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Click")
    def click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem

    def scroll_and_click(self, locator, timeout=None) -> WebElement:
        elem = self.wait(timeout).until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        return elem

    def go_to_new_tab(self):
        handles = self.driver.window_handles
        assert len(handles) > 1
        self.driver.switch_to.window(handles[1])

    def is_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_invisible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
