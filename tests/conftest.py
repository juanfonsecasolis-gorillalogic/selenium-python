from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    yield my_driver
    my_driver.quit()