from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize Safari WebDriver
driver = webdriver.Safari()
driver.get(url='https://www.lambdatest.com')

print(driver.page_source) # код сайта


email_form = driver.find_element(by=By.ID,value='__next')

