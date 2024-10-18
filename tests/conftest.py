from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def getDriver(browser):
    print(f'Creating {browser} driver.')
    if browser=="Chrome":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--remote-debugging-pipe')
        return webdriver.Chrome(
            options=options,
            service=Service(ChromeDriverManager().install())
        )
    elif browser=="Safari":
        return webdriver.Safari()
    else:
        raise NotImplementedError(f'Unknown browser {browser}.')

@pytest.fixture()
def driver(request):
    my_driver = getDriver(
        request.config.getoption("--browser")
    )
    yield my_driver
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default="Chrome",
        help="Browser to execute tests (Chrome or Safari)."
    )