import pytest as pytest

# (ChromeDriverManager().install())
from selenium.webdriver.support.wait import WebDriverWait
import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(request):
    ch1_capabilities = {
        "browserName": "chrome"}
    ch2_capabilities = {
        "browserName": "firefox"}

    ch1_driver = webdriver.Remote(
        command_executor='http://192.168.88.189:4444',
        desired_capabilities=ch1_capabilities)
    ch2_driver = webdriver.Remote(
        command_executor='http://192.168.88.189:4444',
        desired_capabilities =ch2_capabilities)
    driver_nodes = [ch1_driver]
    for driver_node in driver_nodes:
        driver = driver_node
        request.instance.driver = driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield
        driver.stop_client()
        driver.close()
        driver.quit()

    driver_nodes1 = [ch2_driver]
    for driver_node in driver_nodes1:
        driver = driver_node
        request.instance.driver = driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield
        driver.stop_client()
        driver.close()
        driver.quit()








    #     "browserName": "chrome",
    #     "browserVersion": "latest",
    #     "platformName": "LINUX",
    # })
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # options = ChromeOptions()
    # options.add_argument("start-maximized")
    # options.set_capability("browserName", "chrome")
    # return webdriver.Remote("http://192.168.88.189:5555", options=options)
    # driver.implicitly_wait(10)
    # driver.maximize_window()
    # wait = WebDriverWait(driver, 10)
    # request.cls.driver = driver
