#Task 2 Doggy age
class Dog:
    age_factor = 7
    def __init__(self,dog_age):
        self.dog_age = dog_age
    def human_age(self):
        return self.dog_age * self.age_factor

test_dog = Dog(6)

print(test_dog.human_age())