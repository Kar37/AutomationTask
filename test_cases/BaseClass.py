import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from mock_constants.constants import BASEURL
from mock_constants.user_data import USER_EMAIL, USER_PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE
from mock_constants.locators import (USERNAME_LOCATOR_ID, PASSWORD_LOCATOR_ID, LOGIN_BUTTON_LOCATOR_ID,
                                     CHECKOUT_FIRST_NAME_ID, CHECKOUT_LAST_NAME_ID, CHECKOUT_POSTAL_CODE_NAME_ID)


class BaseClass:
    def login_with_credentials(self, driver, username, password):
        driver.find_element(By.ID, USERNAME_LOCATOR_ID).clear()
        driver.find_element(By.ID, USERNAME_LOCATOR_ID).send_keys(username)
        driver.find_element(By.ID, PASSWORD_LOCATOR_ID).clear()
        driver.find_element(By.ID, PASSWORD_LOCATOR_ID).send_keys(password)

    def fill_checkout_credentials(self, logged_driver, firstname, lastname, postalcode):
        logged_driver.find_element(By.ID, CHECKOUT_FIRST_NAME_ID).clear()
        logged_driver.find_element(By.ID, CHECKOUT_FIRST_NAME_ID).send_keys(firstname)
        logged_driver.find_element(By.ID, CHECKOUT_LAST_NAME_ID).clear()
        logged_driver.find_element(By.ID, CHECKOUT_LAST_NAME_ID).send_keys(lastname)
        logged_driver.find_element(By.ID, CHECKOUT_POSTAL_CODE_NAME_ID).clear()
        logged_driver.find_element(By.ID, CHECKOUT_POSTAL_CODE_NAME_ID).send_keys(postalcode)

    def click(self, driver, locator, value):
        driver.find_element(locator, value).click()

    # def click_on_nth_element(self, elements, n, wait_before=0.5, wait_after=1.5):
    #     time.sleep(wait_before)
    #     elements[n].click()
    #     time.sleep(wait_after)

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(BASEURL)
        return driver

    @pytest.fixture(name='logged_driver')
    def login(self, driver):
        self.login_with_credentials(driver, USER_EMAIL, USER_PASSWORD)
        self.click(driver, By.ID, LOGIN_BUTTON_LOCATOR_ID)
        return driver
