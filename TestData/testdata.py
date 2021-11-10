import json
from Objects.product import Product
from Utils.Utility import Utility
from Objects.checkout import Checkout

class TestData(object):
    BROWSER_NAME = 'Chrome'
    TEST_FILE = '../TestData/data.json'
    BASE_URL = 'https://demo.gondolatest.com/'

    @staticmethod
    def get_product():
        product_list = []
        data = Utility().rear_json(TestData.TEST_FILE)

        for item in data['product']:
            list = Product(item["name"], item["price"])
            product_list.append(list)

        return product_list

    @staticmethod
    def get_checkout():
        data = Utility().rear_json(TestData.TEST_FILE)

        checkout = data['checkout_info']
        email = checkout['email']
        card_number = checkout['card']
        exp_date = checkout['date']
        cvc = checkout['cvc']
        postal = checkout['postal']

        checkout_info = Checkout(email, card_number, exp_date, cvc, postal)
        return checkout_info