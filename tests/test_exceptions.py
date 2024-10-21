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

        # wait for the second row to load
        wait = WebDriverWait(driver, timeout=10)
        secondRowElement = wait.until(ec.presence_of_element_located((By.XPATH, '(//*[@class="input-field"])[2]')))
        
        assert secondRowElement.is_displayed, 'Expected a second row.'
    
    @pytest.mark.exception
    @pytest.mark.element_not_interactable_exception
    def test_element_not_interactable_exception(self, driver):
        driver.get(f'{base_url}/practice-test-exceptions')
        driver.find_element(By.ID, 'add_btn').click()

        # wait for the second row to load
        wait = WebDriverWait(driver, timeout=10)
        secondRowElement = wait.until(ec.presence_of_element_located((By.ID, 'row2')))
        
        # save some text in the second row
        secondRowElement.find_element(By.XPATH, './input').send_keys("Testing element not interactable exception...")
        secondRowElement.find_element(By.ID, 'save_btn').click()

        assert driver.find_element(By.ID, 'confirmation').text=='Row 2 was saved'