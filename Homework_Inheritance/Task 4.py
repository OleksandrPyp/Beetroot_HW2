#Task 4 Custom exception
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        with open ("logs.txt", "a") as f:
            f.write(message + "\n")

