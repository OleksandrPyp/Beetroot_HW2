#Task 1
import re


class Email:
    def __init__(self, email):
        self.email = self.validate(email)

    @classmethod
    def validate(cls, email):
        valid_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(valid_email, email):
            raise ValueError("Invalid email address")
        return email


tst = Email("1Oleks-@pypenko.com")
tst1 = Email("11111")

print(tst.validate("1Oleks-@pypenko.com"))