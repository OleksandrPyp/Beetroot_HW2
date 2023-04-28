#Task 1 Method overloading
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        raise NotImplementedError("Function must be implemented in a sub class")


class Capibara(Animal):
    def speak(self):
        print("OMG aren't I'm the cutest animal in the world?")


class Quokka(Animal):
    def speak(self):
        print("Hold my beer, I'm a cutie pie as well")


cutest_animals = [Capibara("Klara"), Quokka("Mokka")]
for i in cutest_animals:
    i.speak()
