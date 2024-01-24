from selenium.webdriver.common.by import By
from test_cases.BaseClass import BaseClass
import time
from mock_constants.constants import VALUE_IS_REQUIRED
from mock_constants.locators import (LOGIN_BUTTON_LOCATOR_ID, LOGOUT_BUTTON_LOCATOR_ID,
                                     VALUE_REQUIRED_MESSAGE_LOCATOR_XPATH)
from mock_constants.user_data import USER_EMAIL, USER_PASSWORD, VOID_EMAIL_PWD

class TestLogin(BaseClass):
    def test_successful_login(self, logged_driver):
        # time.sleep(3)
        logout_exists = logged_driver.find_element(By.ID, LOGOUT_BUTTON_LOCATOR_ID)
        assert logout_exists

    def test_fail_login(self, driver):
        self.login_with_credentials(driver, VOID_EMAIL_PWD, VOID_EMAIL_PWD)
        self.click(driver, By.ID, LOGIN_BUTTON_LOCATOR_ID)
        # time.sleep(3)
        login_error_message = driver.find_element(By.XPATH, VALUE_REQUIRED_MESSAGE_LOCATOR_XPATH)
        assert VALUE_IS_REQUIRED in login_error_message.text

        # print(login_error_message.text)
