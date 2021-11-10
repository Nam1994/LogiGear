import time
from Pages.cart_page import CartPage
from TestCases.base_test import BaseTest
from TestData.testdata import TestData
from Pages.check_out_cart_page import CheckOutCartPage

import unittest

from Utils.assertion import Assertion


class TestCartPage(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_cart_page_successfully(self):
        menu_page = CartPage(self.driver)
        dict = TestData.get_product()
        for i in dict:
            print(i)


if __name__ == "__main__":
    unittest.main()
