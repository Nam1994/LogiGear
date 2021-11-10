from selenium.webdriver.common.by import By


class CheckOutLocator(object):

    @staticmethod
    def NAME(index):
        return By.XPATH, "((//div[@class='cartitems'])[" + str(index) + "])/div[@class='carttext']/h4"

    @staticmethod
    def PRICE(index):
        return By.XPATH, "(((//div[@class='cartitems'])[" + str(index) + "])/div[@class='carttext']/p)[1]"

    TOTAL_ITEM = (By.CLASS_NAME, 'cartcount')

    EMAIL_INPUT = (By.ID, 'email')
    IFRAME = (By.XPATH, "//div[@class='payment']//iframe")
    CARD_NUMBERS_INPUT = (By.XPATH, "//input[@name='cardnumber']")
    EXP_DATE_INPUT = (By.XPATH, "//input[@name='exp-date']")
    CVC_INPUT = (By.XPATH, "//input[@name='cvc']")
    POSTAL_INPUT = (By.XPATH, "//input[@name='postal']")

    PAY_CREDIT_CART_BUTTON = (By.XPATH, "//button[text()='Pay with credit card']")
