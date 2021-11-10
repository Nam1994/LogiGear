import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.gondolatest.com/")

driver.find_element(By.XPATH, "//li[contains(text(), 'W')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[contains(text(), 'M')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//li[contains(text(), 'S')]").click()

source1 = driver.find_element(By.ID, 'pricerange')
action = ActionChains(driver)
action.drag_and_drop_by_offset(source1, 27, 0).perform()
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)
driver.execute_script("window.scrollBy(0, -700);")
time.sleep(4)

driver.find_element(By.XPATH,
                    "((//section[@class='content']/div[@class='item'])[1])/button[text()='Add To Cart']").click()
driver.find_element(By.XPATH, "//div[@class='cartitem']").click()
name_info = driver.find_element(By.XPATH, "//div[@class='cartitems']//h4").text
price_info = driver.find_element(By.XPATH, "(//div[@class='cartitems']//p)[1]").text
total_item = driver.find_element(By.XPATH, "//div[@class='cartitems']//strong").text

print("name is %s, prices is %s, total item is %s " % (name_info, price_info, total_item))

driver.find_element(By.ID, 'email').send_keys("nam.ngh94@gmail.com")
iframe = driver.find_element(By.XPATH, "//div[@class='payment']//iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//input[@name='cardnumber']").send_keys('4242 4242 4242 4242')
driver.find_element(By.XPATH, "//input[@name='exp-date']").send_keys('1221')
driver.find_element(By.XPATH, "//input[@name='cvc']").send_keys('012')
driver.find_element(By.XPATH, "//input[@name='postal']").send_keys('70000')
driver.switch_to.default_content()
driver.find_element(By.XPATH, "//button[text()='Pay with credit card']").click()

time.sleep(3)
driver.quit()
