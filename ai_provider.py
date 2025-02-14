from g4f.client import Client


class AI:
    def __init__(self, model:str = 'free'):
        if model == 'free':
            self.client = Client()
            self.model = "gpt-4o-mini"
        elif model == 'gpt':
            ...
        elif model == 'deepseek':
            ...

    def translate(self, text:str = '', lang:str = 'ru'):
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

    def decompose(self, task: str = '', lang:str = 'ru'):
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



ai = AI()
# print(ai.translate(text='fuck off boy', lang='ru'))
print(ai.decompose(task='Необходимо написать сайт на fast api чтобы выполнить заказ для интернет магазина', lang='ru'))
