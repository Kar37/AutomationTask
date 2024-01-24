import time

from test_cases.BaseClass import BaseClass
from mock_constants.locators import ADD_TO_CART_XPATH, CART_ICON_XPATH, SAUCE_LABS_BACKPACK_XPATH
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


