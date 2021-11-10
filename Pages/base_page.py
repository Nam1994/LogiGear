import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def navigate(self, url):
        message = "Navigate to '{}'"
        logging.info(message.format(url))
        self.driver.implicitly_wait(self.timeout)
        self.driver.get(url)

    def enter_text(self, by_locator, text):
        message = "Enter value '{}' into the element with locator '{}'"
        logging.info(message.format(text, ','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def submit_form(self, by_locator):
        message = "Submit form with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.submit()

    def click(self, by_locator):
        message = "Submit form with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.click()

    def get_elements(self, by_locator):
        message = "Submit form with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        elements = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return elements

    def get_text(self, by_locator):
        message = "Get text of the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def back_browser(self):
        self.driver.back()

    def is_visible(self, by_locator):
        message = "Check the element with the locator '{}' is visible or not"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return bool(element)