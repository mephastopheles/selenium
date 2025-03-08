from g4f.client import Client

import logging
from logging.handlers import RotatingFileHandler
from selenium import webdriver

# logger config
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Setup logger
logger = logging.getLogger(__name__)

logger.addHandler(RotatingFileHandler(filename=f"logs/{__name__}.log",
                                      mode='w',
                                      maxBytes=1024 * 1024))


class AI:
    def __init__(self, model: str = 'free'):
        if model == 'free':
            self.client = Client()
            self.model = "gpt-4o-mini"

        # платные модели
        elif model == 'gpt':
            ...
        elif model == 'deepseek':
            ...

    def translate(self, text: str = '', lang: str = 'ru'):
        """
        Translates data through LLM

        Args:
            text (str): Text for translation
            lang (str): Language code
        """
        try:
            content = f"Please translate the following text to {lang}. Text: {text}"
            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model
            )

            return response.choices[0].message.content
        except Exception as e:
            print(f"Failed to translate via LLM: {e}")

    def decompose(self, task: str = '', lang: str = 'ru'):
        """
        Decomposes task through LLM

        Args:
            task (str): Task for decompose
            lang (str): Language code
        """
        try:
            content = f'Please decompose the following task. Task: {task}'
            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'Failed to decompose via LLM {e}')

    def extract_pd(self, task: str = '', lang: str = 'ru'):
        """
        Extract personal data from task through LLM

        Args:
            task (str): Task for decompose
            lang (str): Language code
        """
        try:
            content = (f'Please extract personal data like '
                       f'name, surname, e-mail, phone, age, password, login, dates, etc'
                       f'from the following task.'
                       f'Task: {task}')
            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'Failed to decompose via LLM {e}')

    # возможно стоит добавить экстрактор url из сообщения
    def generate(self, decomposed_task: str, url: str, page_source: str, pd: dict = None, lang: str = 'ru'):
        """
        Generates code with selenium for decomposed task on url through LLM

        Args:
            lang (str): Language code
            pd (dict): Personal data dictionary
            page_source (str):  code of sites page
            url (str): task page
            decomposed_task (str): Decomposed task for completes


        Returns:
            code on python
        """
        if len(page_source) > 150:
            page_source = page_source[:150]

        try:
            if pd is None:

                content = (
                    f'Please generate code for complete the following task on {url} with python framework selenium.'
                    f'The page at the {url} has the following structure {page_source}.'
                    f'Task: {decomposed_task}')
            else:
                content = (
                    f'Please generate code for complete the following task on {url} with python framework selenium.'
                    f'The page at the {url} has the following structure  {page_source}.'
                    f'Task: {decomposed_task}.'
                    f'Personal data for task: {pd}.')
            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'Failed to generate code via LLM {e}')

    def rewrite(self, code: str, error: str, lang: str = 'ru'):
        """
        Rewrite code with error through LLM

        Args:
            lang (str): Language code
            error (str): Error
            code (str): Code


        Returns:
            code on python
        """

        try:

            content = (f'This code {code} raises error {error}. Please rewrite code.')

            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'Failed to generate code via LLM {e}')


if __name__ == '__main__':
    ai = AI()
    url = 'https://google.com'
    driver = webdriver.Safari()
    driver.get(url=url)
    page_source = driver.page_source
    driver.quit()
    code = ai.generate(decomposed_task='бля буду буди', url='https://google.com', pd=None, page_source=page_source)
    pass
