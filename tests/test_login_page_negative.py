from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

base_url = 'https://practicetestautomation.com'

class TestNegativeScenarios:

    @pytest.mark.negative
    def test_negative_username(self):
        driver = webdriver.Chrome()
        driver.get(f'{base_url}/practice-test-login')
        driver.find_element(By.ID, 'username').send_keys('student123')
        driver.find_element(By.ID, 'password').send_keys('Password123')
        driver.find_element(By.ID, 'submit').click()
        errorElement = driver.find_element(By.ID, "error")
        assert errorElement.is_displayed, 'System should have displayed an error message.'
        assert errorElement.text=='Your username is invalid!', 'Error message is not expected'
        assert driver.current_url == f'{base_url}/practice-test-login/'
        driver.close()

    @pytest.mark.negative
    def test_negative_password(self):
        driver = webdriver.Chrome()
        driver.get(f'{base_url}/practice-test-login')
        driver.find_element(By.ID, 'username').send_keys('student')
        driver.find_element(By.ID, 'password').send_keys('PasswordABC')
        driver.find_element(By.ID, 'submit').click()
        errorElement = driver.find_element(By.ID, "error")
        assert errorElement.is_displayed, 'System should have displayed an error message.'
        assert errorElement.text=='Your password is invalid!', 'Error message is not expected'
        assert driver.current_url == f'{base_url}/practice-test-login/'
        driver.close()