from docx import Document


class DOCXParser:
    """class for parsing docx objects"""


    def __init__(self, filepath: str):
        self.filepath = filepath
        self.document = Document(self.filepath)
        self.text = []

    def output_result(self):
        for para in self.document.paragraphs:
            self.text.append(para.text)

        return '\n'.join(self.text)

    def result(self):
        return '\n'.join(self.text)

    def save(self):
        self.document.save(self.filepath)


if __name__ == '__main__':
    pass
