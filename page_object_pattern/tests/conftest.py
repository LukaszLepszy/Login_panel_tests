import pytest as pytest

# (ChromeDriverManager().install())
from selenium.webdriver.support.wait import WebDriverWait
import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    yield
    driver.stop_client()
    driver.close()
    driver.quit()
