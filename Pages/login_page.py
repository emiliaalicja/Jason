from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

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

    def input_name(self):
        pass


