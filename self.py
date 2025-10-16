#We a creating a method for a class without any parameter and then execute it to see what it is going to print

class Employee:
    def employee_details(self):
        return self.name
max = Employee()
max.name =  "Maximo Gutierrez"

print(max.employee_details())

class Dog:
    def print_info(self):
        self.breed = "Boston terrier"
        print("Breed: ", self.breed)
        name = "Nacho"
        print("Name: ", name)
    
    def talk(self):
        print("Hi, my name is ", self.name, " and I am a ", self.breed)

nacho = Dog()
nacho.print_info()
nacho.talk()