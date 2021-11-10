import logging
import time
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Objects.product import Product
from Locators.cart_page_locator import CartLocator
from TestData.testdata import TestData
from Pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(TestData.BASE_URL)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_title_on_header(self):
        self.click(CartLocator.WOMEN_LABEL)
        time.sleep(3)
        self.click(CartLocator.MEN_LABEL)
        time.sleep(3)
        self.click(CartLocator.SALE_LABEL)
        time.sleep(3)

    def find_item_by_scrollbar(self):
        scroll_bar = self.driver.find_element(*CartLocator.PRICE_BUTTON)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(scroll_bar, 27, 0).perform()
        time.sleep(3)
        print(scroll_bar.get_attribute('value'))
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -700);")
        time.sleep(2)

    def home_page(self):
        self.click(CartLocator.HOMEPAGE_LOGO)

    def add_product_to_cart(self, index):
        self.click(CartLocator.ADD_ITEM(index))

    def get_product_info(self, index):
        name = self.get_text(CartLocator.NAME(index))
        price = self.get_text(CartLocator.PRICE(index))

        product = Product(name, price)
        return product

    def total_item(self):
        self.get_text(CartLocator.TOTAL_ITEM)
