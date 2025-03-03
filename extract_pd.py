import re


class PDExtractor:
    """personal data extractor"""
    # надо бы добавить ещё каких нибудь разных данных
    def __init__(self, message: str):
        self.message = message

    def email_extractor(self):
        if re.search(r'mail', self.message, flags=re.IGNORECASE):
            match = re.search(pattern=r'\s[A-Z0-9. _%+-]+@[A-Z0-9.-]+\.[ A-Z]{2,}($\s)',
                              string=self.message,
                              flags=re.IGNORECASE)
            if match:
                return match.group(0)[1:]

    def name_extractor(self):
        if re.search(pattern=r'name',
                     string=self.message,
                     flags=re.IGNORECASE):
            match = re.search(pattern=r'\s\D+($|\s)',
                              string=self.message,
                              flags=re.IGNORECASE)
            if match:
                return match.group(0)[1:]

    def phone_extractor(self):
        if re.search(pattern=r'phone',
                     string=self.message,
                     flags=re.IGNORECASE):
            match = re.search(pattern=r'\s[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}($|\s)',
                              string=self.message,
                              flags=re.IGNORECASE)
            if match:
                return match.group(0)[1:]


if __name__ == '__main__':
    pass
