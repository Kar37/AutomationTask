from test_cases.BaseClass import BaseClass

class TestTitle(BaseClass):

    def test_home_page_title(self, driver):
        assert driver.title == "Swag Labs"
