import time
from telnetlib import EC

import pytest
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

    def properly_loggining(self):
        self.driver.get(self.sign_in_page)
        self.login_properly_credential()
        self.wait_until_visibility_css(self.header_navigation)

    def get_name_header(self):
        element = self.get_text(self.header_navigation)
        return element

    def get_notyfication_and_tooltip(self):
        self.driver.get(self.sign_in_page)
        self.wait_until_clicable_css(self.sign_in_button)
        self.click_on_element_css(self.sign_in_button)
        self.wait_until_visibility_css(self.notyfication)
        self.wait_until_visibility_css(self.tooltip)

    def get_tooltip_message(self):
        self.get_notyfication_and_tooltip()
        element = self.get_text(self.tooltip)
        return element

        