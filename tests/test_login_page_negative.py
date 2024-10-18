from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait

base_url = 'https://practicetestautomation.com'

class TestNegativeScenarios:

    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.parametrize('username, password, expected_error_message', 
                             [('incorrectUser', 'Password123', 'Your username is invalid!'), 
                              ('student', 'PasswordABC', 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, expected_error_message):
        driver.get(f'{base_url}/practice-test-login')
        driver.find_element(By.ID, 'username').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'submit').click()
        errorElement = driver.find_element(By.ID, "error")
        assert errorElement.is_displayed, 'System should have displayed an error message.'
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda d: errorElement.text==expected_error_message)
        assert errorElement.text==expected_error_message, 'Error message is expected.'
        assert driver.current_url == f'{base_url}/practice-test-login/'
