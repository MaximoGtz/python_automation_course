class Employee:
    def instance_employee(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def say_hi(self):
        print("Hello, my name is ", self.name, ", I am ", self.age, " years old. My occupation is ", self.occupation)

max = Employee()
max.instance_employee("Maximo", 24, "Automation Tester")
max.say_hi()

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def say_hi(self):
        print("Hi, I am ", self.name, " I am a ", self.breed, " and I am ", self.age," years old.")

nacho = Dog("Nacho", "Boston terrier", 4)
nacho.say_hi()