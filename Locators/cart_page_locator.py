from selenium.webdriver.common.by import By


class CartLocator(object):
    """Home page"""
    PRICE_BUTTON = (By.ID, 'pricerange')
    WOMEN_LABEL = (By.XPATH, "//li[contains(text(), 'W')]")
    MEN_LABEL = (By.XPATH, "//li[contains(text(), 'M')]")
    SALE_LABEL = (By.XPATH, "//li[contains(text(), 'S')]")
    HOMEPAGE_LOGO = (By.CLASS_NAME, "logo")
    SHOPPING_CART_LOGO = (By.CLASS_NAME, "cartcount")

    @staticmethod
    def ADD_ITEM(index):
        return By.XPATH, "((//section[@class='content']/div[@class='item'])[" + str(index) + "])/button[text()='Add To " \
                                                                                             "Cart'] "

    @staticmethod
    def NAME(index):
        return By.XPATH, "(((//section[@class='content']/div[@class='item'])[" + str(index) + "])/p)[1]"

    @staticmethod
    def PRICE(index):
        return By.XPATH, "(((//section[@class='content']/div[@class='item'])[" + str(index) + "])/p)[2]"

    @staticmethod
    def IMAGE(index):
        return By.XPATH, "((//section[@class='content']/div[@class='item'])[" + str(index) + "])/img"

    TOTAL_ITEM = (By.XPATH, "//div[@class='cartitem']/div[@class='cartcount']")