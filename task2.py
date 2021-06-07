# TODO: Task 2
#   Doggy age
#   Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s
#   age. Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self, age_factor):
        total_age = self.age*self.age_factor
        return total_age

final_age = Dog(age=int(input('Input age: ')))
print(final_age.human_age(age_factor=()))
