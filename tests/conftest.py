from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--remote-debugging-pipe')
    my_driver = webdriver.Chrome(
        options=options,
        service=Service(ChromeDriverManager().install())
    )
    yield my_driver
    my_driver.quit()