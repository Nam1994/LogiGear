import os
import unittest
from selenium import webdriver
from TestData.testdata import TestData


class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = self.getBrowser()
        print('browser', browser)
        self.driver = self.launchBrowser(browser)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def launchBrowser(browserName='chrome'):
        try:
            if browserName.lower() == 'firefox':
                return webdriver.Firefox()
            elif browserName.lower() == 'firefox':
                return webdriver.Ie()
            elif browserName.lower() =='lambda':
                username = "namb1209103"  # Replace the username
                access_key = "TLId6dMrSVR4RBe6AZNmhuuGPOH7v5oo1pqq0MBOzdxf36DIiY"  # Replace the access key

                desired_caps = {
                    "build": 'PyunitTest the openweathers web',  # Change your build name here
                    "name": 'Py-unittest',  # Change your test name here
                    "platform": 'Windows 10',  # Change your OS version here
                    "browserName": 'Chrome',  # Change your browser here
                    "version": '92.0',  # Change your browser version here
                    "resolution": '1024x768',  # Change your resolution here
                    "console": 'true',  # Enable or disable console logs
                    "network": 'true'  # Enable or disable network logs
                }
                return webdriver.Remote(
                    command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
                    desired_capabilities=desired_caps)
            else:
                return webdriver.Chrome()
        except Exception as msg:
            print("Launch Browser: %s" % str(msg))

    @staticmethod
    def getBrowser():
        try:
            return os.environ['BROWSER_NAME']
        except:
            return TestData.BROWSER_NAME
