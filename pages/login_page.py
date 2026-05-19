from utils.base_page import BasePage
from locators.login_locator import LoginLocator
from locators.home_locators import HomeLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#class for loginpage working steps
class LoginPage(BasePage):
    def open_login_page(self):
        self.click(LoginLocator.login_btn)

    def login(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginLocator.login_btn)
        )
        self.click(LoginLocator.login_btn)

    def is_login_btn_visible(self):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(LoginLocator.login_btn)
            ).is_displayed()
        except:
            return False

    def is_login_visible(self):
        return self.find_visible(HomeLocator.email_field).is_displayed()

    def login_with_id(self, email, password):
        self.send_keys(HomeLocator.email_field, email)
        self.send_keys(HomeLocator.password_field, password)
        self.click(HomeLocator.sub_btn)

    def login_with_invalid_id(self, email, password):
        self.send_keys(HomeLocator.email_field, email)
        self.send_keys(HomeLocator.password_field, password)
        self.click(HomeLocator.sub_btn)

    def open_dropdown(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*HomeLocator.drop_down).is_displayed()
        )
        self.click(HomeLocator.drop_down)

    def sign_out(self):
        try:
            self.open_dropdown()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomeLocator.sign_out)
            )

            el = self.driver.find_element(*HomeLocator.sign_out)
            self.driver.execute_script("arguments[0].click();", el)

        except Exception as e:
            print("Logout failed:", e)
            raise


