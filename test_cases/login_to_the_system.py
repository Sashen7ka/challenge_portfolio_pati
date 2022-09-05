import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_log_in_to_the_system(self):
       self.user_login.title_of_page()
       self.user_login.title_of_header()
       self.user_login.do_login('user01@getnada.com', 'Test-1234')
       self.dashboard_page.title_of_page()
       time.sleep(5)


    def test_incorrect_login_to_the_system(self):
        self.user_login.do_login('test', 'Test-1234')
        self.user_login.incorrect_login_check_message()
        self.user_login.title_of_page()
        time.sleep(5)

    def test_empty_password(self):
        self.user_login.do_login('user01@getnada.com', '')
        self.user_login.empty_password_check_message()
        self.user_login.title_of_page()
        time.sleep(5)

    def test_log_out(self):
        self.user_login.do_login('user01@getnada.com', 'Test-1234')
        self.dashboard_page.wait_for_sign_out_will_be_visible()
        self.dashboard_page.click_on_sign_out_button()
        self.user_login.title_of_page()
        time.sleep(5)

    def test_remind_password(self):
        self.user_login.click_on_remind_password()
        self.user_login.check_remind_page_title()
        self.user_ligin.type_in_email('user01@getnada.com')





