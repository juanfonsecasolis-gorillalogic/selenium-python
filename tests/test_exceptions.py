from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

base_url = 'https://practicetestautomation.com'

class TestException:

    @pytest.mark.exception
    def test_not_such_element_exception(self, driver):
        driver.get(f'{base_url}/practice-test-exceptions')
        driver.find_element(By.ID, 'add_btn').click()

        wait = WebDriverWait(driver, timeout=10)
        secondRowElement = wait.until(ec.presence_of_element_located((By.XPATH, '(//*[@class="input-field"])[2]')))
        
        assert secondRowElement.is_displayed, 'Expected a second row.'
        