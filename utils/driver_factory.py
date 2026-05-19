from selenium import webdriver

#function to work on cross browser
def get_driver(browser='chrome'):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception('browser must be chrome or firefox')
    return driver