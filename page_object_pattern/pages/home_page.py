import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object_pattern.locators.home_page_locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def put_email(self, key):
        self.send_key_xpath(self.email_input, key)

    def put_password(self, key):
        self.send_key_xpath(self.password_input, key)

    def login_properly_credential(self):
        self.put_email("tester.mail@o2.pl")
        self.put_password("12345678")
        self.click_on_element_css(self.sign_in_button)

    def wait_to_visibility_rechapta(self):
        self.login_properly_credential()
        self.wait_until_visibility_css(self.reChapta_window)

