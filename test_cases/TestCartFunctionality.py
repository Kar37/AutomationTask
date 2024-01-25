import time

from test_cases.BaseClass import BaseClass
from mock_constants.locators import (ADD_TO_CART_XPATH, CART_ICON_XPATH, SAUCE_LABS_BACKPACK_XPATH, CHECKOUT_BUTTON_ID,
                                     CHECKOUT_FIRST_NAME_ID,
                                     CHECKOUT_LAST_NAME_ID,
                                     CHECKOUT_POSTAL_CODE_NAME_ID,
                                     CHECKOUT_CONTINUE_ID,
                                     CHECKOUT_FINISH_ID,
                                     THANK_YOU_FOR_YOUR_ORDER_XPATH)
from mock_constants.user_data import FIRST_NAME, LAST_NAME, POSTAL_CODE
from mock_constants.constants import ORDER_MASSAGE
from selenium.webdriver.common.by import By


class TestCartFunctionality(BaseClass):

    def test_add_to_cart(self, logged_driver):
        self.click(logged_driver, By.XPATH, ADD_TO_CART_XPATH)
        # time.sleep(2)
        self.click(logged_driver, By.XPATH, CART_ICON_XPATH)
        time.sleep(2)
        product_name = logged_driver.find_element(By.XPATH, SAUCE_LABS_BACKPACK_XPATH)
        assert SAUCE_LABS_BACKPACK_XPATH

        # print(product_name.text)
    def test_end_to_end_order(self, logged_driver):
        self.click(logged_driver, By.XPATH, ADD_TO_CART_XPATH)
        self.click(logged_driver, By.XPATH, CART_ICON_XPATH)
        self.click(logged_driver, By.ID, CHECKOUT_BUTTON_ID)
        # time.sleep(3)
        self.fill_checkout_credentials(logged_driver, FIRST_NAME, LAST_NAME, POSTAL_CODE)
        # time.sleep(2)
        self.click(logged_driver, By.ID, CHECKOUT_CONTINUE_ID)
        # time.sleep(2)
        self.click(logged_driver, By.ID, CHECKOUT_FINISH_ID)
        # time.sleep(1.5)
        successful_order = logged_driver.find_element(By.XPATH, THANK_YOU_FOR_YOUR_ORDER_XPATH)
        assert ORDER_MASSAGE in successful_order.text
        # print(successful_order.text)
