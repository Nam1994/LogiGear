import time
from Pages.cart_page import CartPage
from TestCases.base_test import BaseTest
from TestData.testdata import TestData

import unittest

from Utils.assertion import Assertion


class TestCartPage(BaseTest):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_cart_page_successfully(self):
        menu_page = CartPage(self.driver)

        """the test case to verify the user can display all items in a specific name"""
        menu_page.click_title_on_header()
        menu_page.home_page()

        """the test case to verify user can see all all  """
        menu_page.find_item_by_scrollbar()
        menu_page.home_page()

        """Verify add to cart function"""
        products = []
        for index in [1, 2, 3]:
            products.append(menu_page.get_product_info(index))

        for index, expected_product in enumerate(products, start=1):
            '''Add all products'''
            menu_page.add_product_to_cart(index)
            time.sleep(2)
            actual_product = menu_page.get_product_info(index)
            assertion = Assertion()
            assertion.compare_products(actual_product, expected_product)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
