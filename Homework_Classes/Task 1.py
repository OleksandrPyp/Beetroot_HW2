#Task 1 A person class
class Person:
    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def speak(self) -> str:
        return f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old."

tst1 = Person("Carl", "Johnson", "26")


print(tst1.speak())