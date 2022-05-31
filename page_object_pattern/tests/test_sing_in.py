import time
import pytest

from page_object_pattern.locators.home_page_locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestGoogle:

    def test_properly_loggining_url(self):
        Login = HomePage(self.driver)
        Login.properly_loggining()
        assert Login.get_current_url() == Login.home_page

    def test_check_header_title(self):
        Login = HomePage(self.driver)
        Login.properly_loggining()
        assert Login.get_name_header() == "Test T"

    def test_empty_logiining_notyfication(self):
        Login = HomePage(self.driver)
        assert Login.get_tooltip_message() == "Invalid email or passwordd."
