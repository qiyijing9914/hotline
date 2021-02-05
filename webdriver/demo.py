from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(1)  # 等待3秒

driver.get("http://172.16.25.62/web/#/discover")
print(driver.title)
driver.find_element_by_xpath("//input[@type='text']").send_keys("Jane_cm_qj")
driver.find_element_by_xpath("//input[@type='password']").send_keys("abc@123456")
driver.find_element_by_xpath("//button[@type='button']").click()
time.sleep(5)
driver.close()