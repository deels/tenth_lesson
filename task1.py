#  TODO: Task 1
#   A Person class
#   Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them
#   as attributes. Make another method called talk() which makes prints a greeting from the person containing,
#   for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f'Привет, меня зовут {self.name} {self.surname} и мне {self.age} лет.')

greeting = Person(name=input('Name: '), surname=input('Surname: '), age=input('Age: '))
print(greeting.talk())
