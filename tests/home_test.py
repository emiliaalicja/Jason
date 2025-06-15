from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from tests.base_test import BaseTest
from tests.base_test import BaseTest
from Pages.home_page import HomePage
import os




EMAIL = os.getenv("EMAIL")
TEST_PASSWORD = os.getenv("PASSWORD")


class HomeTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_get_welcome_text(self):
        self.home_page.get_my_account_button()
        welcome_message = self.home_page.get_my_account_button()
        print(welcome_message)
        self.assertEqual(welcome_message, "My account", "Should receive home page and text 'My account")


    def test_my_account_click(self):
        self.home_page.click_my_account_button()
        self.login_page = LoginPage(self.driver)
        self.login_page.input_email(EMAIL)
        self.login_page.input_password(TEST_PASSWORD)
        self.login_page.click_button()

