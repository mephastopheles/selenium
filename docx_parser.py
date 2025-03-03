from docx import Document


class DOCXParser:
    """class for parsing docx objects"""


    def __init__(self, filepath: str):
        self.filepath = filepath
        self.document = Document(self.filepath)
        self.text = []

    def text_extraction(self):
        for para in self.document.paragraphs:
            self.text.append(para.text)

        return '\n'.join(self.text)

    def result(self):
        return '\n'.join(self.text)

    def save(self):
        self.document.save(self.filepath)


if __name__ == '__main__':
    dp = DOCXParser(filepath='xui.docx')
    print(dp.text_extraction())
