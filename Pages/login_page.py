from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import os

class LoginLocators:
    HEADER= (By.XPATH, "//h1[@class='entry-title']")
    USERNAME_REGISTER = (By.ID, "reg_email")
    PASSWORD_REGISTER = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.NAME, "register")

class LoginPage(BasePage):


    def get_header_text(self):
        header_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.HEADER)
        )
        return header_text.text

    def input_email(self, email):
        email = os.environ.get("EMAIL")
        email_input = self.driver.find_element(*LoginLocators.USERNAME_REGISTER)
        email_input.send_keys(email)

    def input_password(self, password):
        TEST_PASSWORD =os.environ.get("TEST_PASSWORD")
        password_input = self.driver.find_element(*LoginLocators.PASSWORD_REGISTER)
        password_input.send_keys(TEST_PASSWORD)

    def click_button(self):
        self.driver.find_element(*LoginLocators.REGISTER_BUTTON).click()




