from locators.home_locators import HomeLocator
from utils.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#class for homepage working steps
class HomePage(BasePage):
    def is_signup_btn_visible(self):
        return self.find_visible(HomeLocator.signup_btn).is_displayed()

    def signup_btn(self):
        self.click(HomeLocator.signup_btn)

    def is_live_class_displayed(self):
        return self.find_visible(HomeLocator.live_class)

    def is_courses_displayed(self):
        return self.find_visible(HomeLocator.courses).is_displayed()

    def is_practice_displayed(self):
        return self.find_visible(HomeLocator.practice).is_displayed()

    def is_dobby_visible(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(HomeLocator.chat_box)
            )

            el = self.driver.find_element(*HomeLocator.chat_box)
            return el.is_displayed()

        except:
            return False


