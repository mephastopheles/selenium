from pdf_parser import PDFParser
from docx_parser import DOCXParser
from extract_pd import PDExtractor
from ai_provider import AI
from selenium import webdriver

if __name__ == '__main__':


    # подключаем АИ
    ai = AI(model='free')

    # подключаем парсер пдф
    pdf = PDFParser(filepath='path/to/pdf')
    task = pdf.output_result()

    # подключаем парсер докса
    docx = DOCXParser(filepath='path/to/docx')
    task = docx.output_result()

    # или обычное сообщение
    task = 'any task'

    # вытаскиваем данные из задачи АИшкой
    extracted_pd = ai.extract_pd(task=task)

    # забираем данные из ответа АИ
    pde = PDExtractor(message=extracted_pd)
    pd = {'phone': pde.phone_extractor(),
          'name': pde.name_extractor(),
          'email': pde.email_extractor()}

    decomposed = ai.decompose(task=task)

    url = ''

    # получаем код страницы
    driver = webdriver.Safari()
    driver.get(url=url)
    page_source = driver.page_source

    code = ai.generate(decomposed_task=decomposed,
                url=url,
                page_source=page_source,
                pd=pd)
    ...
