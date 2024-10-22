from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

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

    @pytest.mark.exception
    @pytest.mark.invalid_element_state_exception
    def test_invalid_element_state_exception(self, driver):
        driver.get(f'{base_url}/practice-test-exceptions')
        
        # The input field is disabled. Trying to clear the disabled field will throw InvalidElementStateException
        #driver.find_element(By.CLASS_NAME, 'input-field').send_keys("")

        newString = 'Hamburger'
        driver.find_element(By.XPATH, '//div[@id="row1"]/button[@id="edit_btn"]').click()
        row1_input_element = driver.find_element(By.XPATH, '//div[@id="row1"]/input')
        wait = WebDriverWait(driver, timeout=10)
        wait.until(ec.element_to_be_clickable(row1_input_element))
        row1_input_element.clear()
        row1_input_element.send_keys(newString)
        driver.find_element(By.XPATH, '//div[@id="row1"]/button[@id="save_btn"]').click()
        
        assert driver.find_element(By.ID, 'confirmation').text=='Row 1 was saved'
        assert row1_input_element.get_attribute('value')==newString
        

