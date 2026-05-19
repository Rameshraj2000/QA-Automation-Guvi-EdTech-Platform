from locators.login_locator import LoginLocator
from pages.login_page import LoginPage

# Test Validate URL
def test_url(driver):
    assert "guvi.in" in driver.current_url

# Test Verify Title of the webpage
def test_valid_title(driver):
    assert driver.title == "HCL GUVI | Learn to code in your native language"
