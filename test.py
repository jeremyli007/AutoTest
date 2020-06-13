from selenium import webdriver
import time

url="http://ics.chinasoftinc.com/SignOnServlet"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# time.sleep(5)
# driver.close()

# driver.find_element_by_id('//input[@id="j_username"]').send_keys('174206')
# //*[@id="dl"]/input[1]
driver.find_element_by_xpath('//*[@id="dl"]/input[1]').send_keys('174206')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dl"]/div').send_keys('19931007LJ')
driver.find_element_by_class_name('button').click()
driver.close()

# 什么也没改