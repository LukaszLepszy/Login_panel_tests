import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object_pattern.locators.credencials import *
from page_object_pattern.locators.home_page_locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def put_email(self, key):
        self.wait_until_clicable_xpath(self.email_input)
        self.send_key_xpath(self.email_input, key)

    def put_password(self, key):
        self.wait_until_clicable_xpath(self.password_input)
        self.send_key_xpath(self.password_input, key)

    def login_properly_credential(self):
        self.put_email(credencials['email'])
        self.put_password(credencials['password'])
        self.click_on_element_css(self.sign_in_button)

    def supply_credentials_and_sing_in(self, email, password):
        self.driver.get(self.sign_in_page)
        self.put_email(email)
        self.put_password(password)
        self.click_on_element_css(self.sign_in_button)

    def wait_to_visibility_rechapta(self):
        self.login_properly_credential()
        self.wait_until_visibility_css(self.reChapta_window)

    def properly_loggining(self):
        self.driver.get(self.sign_in_page)
        self.login_properly_credential()
        self.wait_until_visibility_css(self.header_navigation)

    def get_name_header(self):
        element = self.get_text_css(self.header_navigation)
        return element

    def get_notyfication_and_tooltip(self):
        self.driver.get(self.sign_in_page)
        self.wait_until_clicable_css(self.sign_in_button)
        self.click_on_element_css(self.sign_in_button)
        self.wait_until_visibility_css(self.notyfication)
        self.wait_until_visibility_css(self.tooltip)

    def get_tooltip_message(self):
        self.wait_until_visibility_css(self.tooltip)
        element = self.get_text_css(self.tooltip)
        return element

    def get_style_notyfication(self):
        self.wait_until_visibility_css(self.notyfication)
        element = self.get_atribute_form_css_selector(self.notyfication, "style")
        return element
        