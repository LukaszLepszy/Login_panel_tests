import time
import pytest

from page_object_pattern.locators.home_page_locators import HomePageLocators
from page_object_pattern.pages.base_page import BasePage
from page_object_pattern.pages.home_page import HomePage
from page_object_pattern.locators.credencials import *


@pytest.mark.usefixtures("setup")
class TestGoogle:

    def test_properly_loggining_url(self):
        Login = HomePage(self.driver)
        Login.properly_loggining()
        assert Login.get_current_url() == Login.home_page

    def test_check_header_title(self):
        Login = HomePage(self.driver)
        Login.properly_loggining()
        assert Login.get_name_header() == "First L"

    @pytest.mark.parametrize("email, password", [(credencials["email"], credencials["empty"]),
                                                 (credencials["empty"], credencials["password"]),
                                                 (credencials["empty"], credencials["empty"])])
    def test_incorect_loggining_tooltip_message(self, email, password):
        Login = HomePage(self.driver)
        Login.supply_credentials_and_sing_in(email, password)
        assert Login.get_tooltip_message() == "Invalid email or password."

    @pytest.mark.parametrize("email, password", [(credencials["email"], credencials["empty"]),
                                                 (credencials["empty"], credencials["password"]),
                                                 (credencials["empty"], credencials["empty"])])
    def test_incorect_loggining_notyfication_style(self, email, password):
        Login = HomePage(self.driver)
        Login.supply_credentials_and_sing_in(email, password)
        if "display: block;" not in Login.get_style_notyfication():
            raise AssertionError("Wrong style")