from g4f.client import Client

import logging
from logging.handlers import RotatingFileHandler

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
            content = (f'Please extract data like personal data, e-mail, phone, age etc from the following task.'
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

    def generate(self, decomposed_task: str = '', url: str = '', lang: str = 'ru', ):
        """
        Generates code with selenium for decomposed task on url through LLM

        Args:
            decomposed_task (str): Decomposed task for completes
            url (str): Url
            lang (str): Language code
        """

        try:
            content = (f'Please generate code for complete the following task on {url} with python framework selenium.'
                       f'Task: {decomposed_task}')
            response = self.client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": content
                }],
                model=self.model
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f'Failed to generate code via LLM {e}')


ai = AI()

if __name__ == '__main__':
    data = ai.extract_pd(task='Необходимо заполнить поля следующим e mail: sobaka@bk.ru ')
    print(data)
