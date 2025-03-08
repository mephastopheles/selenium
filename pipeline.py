from pdf_parser import PDFParser
from docx_parser import DOCXParser
from extract_pd import PDExtractor
from ai_provider import AI
from selenium import webdriver
import re

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
          'email': pde.email_extractor()}

    decomposed = ai.decompose(task=task)

    url = 'https://app.conneto.com'

    # получаем код страницы
    driver = webdriver.Safari()
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

