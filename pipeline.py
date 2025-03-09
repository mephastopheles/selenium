from pdf_parser import PDFParser
from docx_parser import DOCXParser
from extract_pd import PDExtractor
from ai_provider import AI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def conneto_login(driver, account: str, password: str):
    driver.get(url='https://app.conneto.com/auth/login')
    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div/div/div[1]/form/div[1]/div/input')))
    username_field.send_keys(account)
    password_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div/div/div[1]/form/div[2]/input')))
    password_field.send_keys(password)
    submit_button = driver.find_element(by=By.CLASS_NAME, value="btn__first")
    submit_button.click()


if __name__ == '__main__':

    # подключаем АИ
    ai = AI(model='free')

    # # подключаем парсер пдф
    # pdf = PDFParser(filepath='path/to/pdf')
    # task = pdf.output_result()
    #
    # # подключаем парсер докса
    # docx = DOCXParser(filepath='path/to/docx')
    # task = docx.output_result()

    # или обычное сообщение
    task = 'log in account on site https://conneto.com  password: 123456 e-mail: easygames420@bk.ru'

    # вытаскиваем данные из задачи АИшкой
    extracted_pd = ai.extract_pd(task=task)

    # забираем данные из ответа АИ
    pde = PDExtractor(message=extracted_pd)
    pd = {'phone': pde.phone_extractor(),
          'name': pde.name_extractor(),
          'email': pde.email_extractor(),
          'password': pde.password_extractor()}

    decomposed = ai.decompose(task=task)



    url = 'https://app.conneto.com'

    # получаем код страницы
    driver = webdriver.Safari()

    conneto_login(driver=driver, account=pd['email'], password=pd['password'])

    driver.get(url=url)
    page_source = driver.page_source
    driver.quit()
    code = ai.generate(decomposed_task=decomposed,
                       url=url,
                       page_source=page_source,
                       pd=pd)

    while True:

        result = re.search('```python', code)
        if result:
            try:
                _start = result.span()[1]

                _result = re.search('```', code[_start:])
                _end = _result.span()[0] + _start
                code = code[_start + 1:_end - 1]
                exec(code)
                break
            except Exception as e:
                code = ai.rewrite(code=code, error=f'{e}')
