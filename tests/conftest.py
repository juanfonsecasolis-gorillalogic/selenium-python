from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

IMPLICIT_WAIT_SECONDS = 20

def driver_per_browser(browser):
    print(f'Creating {browser} driver.')
    if browser=="Chrome":
        options = Options()
        #options.add_argument('--headless')
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
    # setup
    my_driver = driver_per_browser(
        request.config.getoption("--browser")
    )
    #my_driver.implicitly_wait(IMPLICIT_WAIT_SECONDS)    # by default 0, DO NOT mix with explicit waits!

    # tear down
    yield my_driver
    my_driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default="Chrome",
        help="Browser to execute tests (Chrome or Safari)."
    )