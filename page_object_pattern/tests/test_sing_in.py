import time
import pytest

from page_object_pattern.locators.home_page_locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestGoogle:

    def test_if_rechapta_appear(self):
        self.driver.get(BasePage.sign_in_page)
        Login = HomePage(self.driver)
        Login.login_properly_credential()
        assert Login.get_current_url() == Login.home_page

