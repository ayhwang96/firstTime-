from selenium import webdriver as wd 
driver = wd.Chrome(executable_path="chromedriver.exe")
url = "https://www.naver.com"
driver.get(url)
from selenium.webdriver.common.by import By
findText = driver.find_element(By.ID, 'query')
findText.send_keys("커피")
B = driver.find_element(By.ID, 'search_btn')
B.click()
A = driver.find_elements_by_css_selector('li.menu')
book = A[9]
book.click()
C = driver.find_elements_by_css_selector('.thumb')

D = driver.find_elements_by_xpath('//li/a/strong')