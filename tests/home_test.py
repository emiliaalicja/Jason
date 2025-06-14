from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from tests.base_test import BaseTest


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



