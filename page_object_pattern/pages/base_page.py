import time

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from page_object_pattern.locators.home_page_locators import HomePageLocators


class BasePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver

    def wait_until_visibility_css(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, by_locator)))

    def wait_until_clicable_css(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, by_locator)))

    def wait_until_invisibility_css(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, by_locator)))

    def wait_until_visibility_xpath(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator)))

    def wait_until_clicable_xpath(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, by_locator)))

    def wait_until_invisibility_xpath(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, by_locator)))

    def wait_until_presence_css(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, by_locator)))

    def wait_until_presence_xpath(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, by_locator)))

    def find_by_css_selector(self, by_locator):
        return self.driver.find_element(By.CSS_SELECTOR, by_locator)

    def find_by_xpath_selector(self, by_locator):
        return self.driver.find_element(By.XPATH, by_locator)

    def find_elements_by_css_selector(self, by_locator):
        return self.driver.find_elements(By.CSS_SELECTOR, by_locator)

    def find_elements_by_xpath_selector(self, by_locator):
        return self.driver.find_elements(By.XPATH, by_locator)

    def select_record_in_dropdown_css(self, by_locator, value):
        select = Select(self.find_by_css_selector(by_locator))
        return select.select_by_value(value)

    def select_record_in_dropdown_xpath(self, by_locator, value):
        select = Select(self.find_by_xpath_selector(by_locator))
        return select.select_by_value(value)

    def send_key_xpath(self, by_locator, key):
        self.wait_until_clicable_xpath(by_locator)
        Webelement = self.find_by_xpath_selector(by_locator)
        Webelement.send_keys(key)

    def execute_click_css(self, by_locator):
        self.wait_until_clicable_css(by_locator)
        element = self.find_by_css_selector(by_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def execute_click_xpath(self, by_locator):
        self.wait_until_clicable_css(by_locator)
        element = self.find_by_xpath_selector(by_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_element_css(self, by_locator):
        self.wait_until_clicable_css(by_locator)
        Webelement = self.find_by_css_selector(by_locator)
        Webelement.click()

    def click_on_element_xpath(self, by_locator):
        self.wait_until_clicable_xpath(by_locator)
        Webelement = self.find_by_xpath_selector(by_locator)
        Webelement.click()

    def submit_css(self, by_locator):
        self.wait_until_clicable_css(by_locator)
        element = self.find_by_css_selector(by_locator)
        element.submit()

    def submit_xpath(self, by_locator):
        self.wait_until_clicable_xpath(by_locator)
        element = self.find_by_xpath_selector(by_locator)
        element.submit()

    def switch_window(self, by_locator):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.wait_until_visibility_css(by_locator)

    def get_text_css(self, by_locator):
        self.wait_until_visibility_css(by_locator)
        text = self.find_by_css_selector(by_locator).text
        return text

    def get_href_css(self, by_locator):
        self.wait_until_visibility_css(by_locator)
        href = self.find_by_css_selector(by_locator).get_attribute("href")
        return href

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def get_atribute_form_css_selector(self, by_locator, atribute):
        self.wait_until_clicable_css(by_locator)
        atrribute_text = self.find_by_css_selector(by_locator).get_attribute(atribute)
        return atrribute_text

    def get_atribute_form_xpath_locator(self, by_locator, atribute):
        self.wait_until_clicable_css(by_locator)
        atrribute_text = self.find_by_xpath_selector(by_locator).get_attribute(atribute)
        return atrribute_text

    def accept_alert_xpath(self, by_locator):
        self.find_by_xpath_selector(by_locator).click()
        time.sleep(4)
        self.driver.switch_to.alert.accept()
        time.sleep(4)

    def dismiss_alert(self, by_locator):
        self.find_by_xpath_selector(by_locator).click()
        time.sleep(4)
        self.driver.switch_to.alert.dismiss()
        time.sleep(4)



