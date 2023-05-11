#Task 1 School
class Person:
    def __init__(self, gender: str, age: int) -> None:
        self.gender = gender
        self.age = age

    def speak(self) -> str:
        return f"Hi I'm {self.gender}, I'm {self.age} y.o"

class Student(Person):
    def __int__(self, name: str, gender: str, age: int, year_of_studies: str, major: str) -> None:
        self.name = name
        self.year_of_studies = year_of_studies
        self.major = major
        super().__init__(self, gender, age)

    def speak(self) -> str:
        return f"Hi I'm Student, my name is {self.name}, I'm {self.gender}, and I'm {self.age} y.o. \n" \
               f"I'm majoring in {self.major} and this is my {self.year_of_studies} year"


class Teacher(Person):
    def __init__(self, name: str, age: int, specialty: str, salary: int) -> None:
        super().__init__(self, age)
        self.name = name
        self.specialty = specialty
        self.salary = salary

    def speak(self) -> str:
        return f"Hi I'm a teacher, my name is {self.name}, I'm {self.age} y.o. I'm teaching {self.specialty}\n" \
               f"and I'm earning {self.salary} "


tst = Teacher("Oleks", 28, "Music", 2800)
print(tst.speak())

