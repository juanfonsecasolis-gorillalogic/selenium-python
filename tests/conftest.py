from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    yield my_driver
    my_driver.quit()