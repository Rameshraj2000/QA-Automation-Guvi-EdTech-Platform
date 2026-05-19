from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)

# Base page contains reusable Selenium methods
# like click, send_keys and wait handling.
class BasePage:

    def __init__(self, driver):
        self.driver = driver
    # function to use whether element is visible in webpage with one argument passed
    def find_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    # function to use whether element is clickable in webpage with one argument passed
    def find_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
    # function to use whether element is present in the webpage with one argument passed
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
    # function to click with one argument passed
    def click(self, locator):

        try:
            el = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el
            )

            time.sleep(2)

            try:
                el.click()

            except:
                self.driver.execute_script(
                    "arguments[0].click();", el
                )

        except TimeoutException:
            print(f"Element not clickable: {locator}")
            raise

    # function to pass keys in the webpage with two arguments passed
    def send_keys(self, locator, text):
        try:
            el = self.find_visible(locator)
            el.clear()
            el.send_keys(text)

        except TimeoutException:
            print(f"Element not found for input: {locator}")
            raise

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 20).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )