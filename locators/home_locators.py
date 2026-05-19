from selenium.webdriver.common.by import By

#class for homepage locators
class HomeLocator:
    signup_btn = (By.XPATH, "(//button[text()='Sign up'])[1]")
    email_field = (By.XPATH, "(//input[@type='email'])[1]")
    password_field = (By.XPATH, "(//input[@type='password'])")
    sub_btn = (By.XPATH, "//a[@id='login-btn']")
    error_msg = (By.XPATH, "(//div[text()='Incorrect Email or Password'])[1]")
    live_class = (By.XPATH, "(//p[contains(text(),'LIVE Classes')])[1]")
    courses = (By.XPATH, "(//p[contains(text(),'Courses')])[1]")
    practice = (By.XPATH, "(//p[contains(text(),'Practice')])[1]")
    chat_box = (By.XPATH, "//span[@id='zs_fl_chat']")
    drop_down = (By.XPATH, "(//img[contains(@class,'rounded-full gravatar')])[1]")
    sign_out = (By.XPATH, "(//p[text()='Sign Out'])[1]")