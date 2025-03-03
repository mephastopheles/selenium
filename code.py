
# пример полученного из LLM кода

# python
# Step 1: Import Required Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# Step 2: Initialize the WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Safari()
# Step 3: Navigate to Google
driver.get("https://www.google.com")

# Step 4: Locate the Google Logo
try:
    logo = driver.find_element(By.XPATH, "//img[@alt='Google']")
    logo.
    print("Google logo found!")
except Exception as e:
    print("Google logo not found:", e)

# Optional: Perform additional actions
# Uncomment the following lines if you want to click the logo or take a screenshot
# logo.click()  # Click the logo
# driver.save_screenshot("google_logo.png")  # Take a screenshot

# Step 5: Close the WebDriver
sleep(60)
driver.quit()
#
# bash
#      pip install selenium webdriver-manager
#
# bash
#      python find_google_logo.py
     
