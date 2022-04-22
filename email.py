class Email:

    def __init__(self, email):
        self.start = int(email.find("@"))
        self.end = int(email.rfind("."))

        if self.start != -1 and self.end != -1 and self.start < self.end:
            self.email = email

    def get_domain(self):
        return self.email[self.start + 1:self.end]
