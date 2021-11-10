import logging
import time
import unittest
from Objects.product import Product
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.checkout_page_locator import CheckOutLocator
from Locators.cart_page_locator import CartLocator
from TestData.testdata import TestData
from Pages.base_page import BasePage


class CheckOutCartPage(BasePage):

    def list_shopping_cart(self):
        self.click(CartLocator.SHOPPING_CART_LOGO)

    def get_product_actual(self, index):
        name = self.get_text(CheckOutLocator.NAME(index))
        price = self.get_text(CheckOutLocator.PRICE(index))

        product_info = Product(name, price)
        return product_info

    def get_total_product(self):
        self.get_text(CheckOutLocator.TOTAL_ITEM)

    def get_checkout_info(self, info):
        self.enter_text(CheckOutLocator.EMAIL_INPUT(), info.email)
        self
