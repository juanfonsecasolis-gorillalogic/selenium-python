from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

base_url = 'https://practicetestautomation.com'

class TestPositiveScearios:

    @pytest.mark.login
    def test_simple_test(self):
        driver = webdriver.Chrome()
        driver.get(f'{base_url}/practice-test-login')
        driver.find_element(By.ID, 'username').send_keys('student')
        driver.find_element(By.ID, 'password').send_keys('Password123')
        driver.find_element(By.ID, 'submit').click()
        assert(driver.current_url == f'{base_url}/logged-in-successfully/')
        assert(driver.find_element(By.TAG_NAME, 'h1').text=='Logged In Successfully')
        assert(driver.find_element(By.LINK_TEXT, 'Log out').is_displayed)
        driver.close()