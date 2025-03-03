import re


with open('code.txt', 'r') as file:
    code = file.read()
# print(code)

result = re.search('```python', code, flags=re.MULTILINE)

print(result)




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main(query):
    # Step 1: Открыть приложение или веб-браузер
    # You can replace 'chrome' with other browsers like 'firefox' if needed.
    driver = webdriver.Safari()

    try:
        # Step 2: Перейти на страницу поиска Google
        driver.get("https://www.google.com")

        # Step 3: Найти строку поиска
        search_box = driver.find_element(By.NAME, "q")

        # Step 4: Напечатать текст в строку поиска
        search_box.send_keys(query)

        # Step 5: Запустить поиск
        search_box.send_keys(Keys.RETURN)

        # Step 6: Просмотреть результаты поиска
        time.sleep(2)  # Wait for results to load

        # Assuming the first result's title and link are of interest
        results = driver.find_elements(By.XPATH, '//h3')
        for index, result in enumerate(results):
            print(f"{index + 1}: {result.text}")

    finally:
        # Close the browser after completing the tasks
        time.sleep(50)  # Wait for a few seconds to review results
        driver.quit()

if __name__ == "__main__":
    # Input for the search query
    search_query = "найти кота"  # The task's search text
    main(search_query)
