import unittest
from selenium import webdriver
from Pages.home_page import HomePage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import tempfile
import os


class BaseTest(unittest.TestCase):
    """
    Base class for each test in one class
    """

    def setUp(self):
        # Chrome w trybie headless (ważne na serwerach)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Tymczasowy profil użytkownika
        tmp_user_data_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={tmp_user_data_dir}")

        # Jawna ścieżka do chromedrivera
        chrome_service = Service(executable_path="/usr/local/bin/chromedriver")

        # Finalna instancja przeglądarki
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://seleniumdemo.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()





# import unittest
# from selenium import webdriver
# from Pages.home_page import HomePage
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import tempfile
#
#
# class BaseTest(unittest.TestCase):
#     """
#     Base class for each test in one class
#     """
#
#     def setUp(self):
#         # Inicjalizacja przeglądarki
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("http://seleniumdemo.com/")
#         self.home_page = HomePage(self.driver)
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")  # tryb bezgłowy - ważne na serwerze
#         chrome_options.add_argument("--no-sandbox")  # potrzebne na serwerach linuxowych
#         chrome_options.add_argument("--disable-dev-shm-usage")  # unika problemów z /dev/shm
#         #chrome_options.add_argument("--disable-gpu")  # może pomóc na starszych systemach
#
#         # Wymuszony unikalny katalog
#         tmp_user_data_dir = tempfile.mkdtemp()
#         chrome_options.add_argument(f"--user-data-dir={tmp_user_data_dir}")
#
#         self.driver = webdriver.Chrome(options=chrome_options)
#
#         # 🔧 Jawna ścieżka do chromedrivera
#         service = Service(executable_path="/usr/local/bin/chromedriver")
#
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver.maximize_window()
#
#
#
#     def tearDown(self):
#         self.driver.quit()
