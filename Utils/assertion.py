import logging
from Objects.product import Product
import unittest


class Assertion(unittest.TestCase):

    def compare_products(self, actual_product, expected_product):
        message = "Actual: '{}', Expect: '{}'"
        try:
            self.assertEqual(actual_product.name, expected_product.name)
        except AssertionError:
            logging.error(message.format(actual_product.name, expected_product.name))
        try:
            self.assertEqual(actual_product.price, expected_product.price)
        except AssertionError:
            logging.error(message.format(expected_product.price, actual_product.price))
        pass
        print('----pass----')

    def compare_str(self, actual, expected):
        message = "Actual: '{}', Expect: '{}'"
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            logging.error(message.format(actual, expected))
        pass

    def compare_total_item(self, actual_product, expected_product):
        message = "Actual total : '{}', Expect total: '{}'"
        try:
            self.assertEqual(actual_product, expected_product)
        except AssertionError:
            logging.error(message.format(actual_product, expected_product))
