from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from Pages.login_page import LoginPage


class Locators:
    MY_ACCOUNT_BUTTON_TEXT= (By.ID, "menu-item-22")

class HomePage(BasePage):


    def get_my_account_button(self):
        my_account_button_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.MY_ACCOUNT_BUTTON_TEXT)
        )
        return my_account_button_text.text

    def click_my_account_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.MY_ACCOUNT_BUTTON_TEXT)
        )
        self.driver.find_element(*Locators.MY_ACCOUNT_BUTTON_TEXT).click()