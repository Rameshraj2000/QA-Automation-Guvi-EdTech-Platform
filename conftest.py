import pytest
from utils.driver_factory import get_driver
from selenium.webdriver.chrome.options import Options

# Pytest fixture for browser setup and teardown
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = get_driver('chrome')
    driver.maximize_window() #maximize window
    driver.get("https://www.guvi.in") #Webpage URL
    yield driver
    driver.quit()