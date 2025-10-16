
class Employee:
#This is a class attribute
    salary = 2300

employee_one = Employee()
employee_two = Employee()
print(employee_one.salary)
print(employee_two.salary)
# You can chande that class attribute whenever you need
# It changes in all instances of the same class
Employee.salary = 2000
print(employee_one.salary)
print(employee_two.salary)

employee_one.name = "John"
employee_two.name = "Deer"
print(employee_one.name)
print(employee_two.name)




#My own example
class Dog:
    breed = "Boston Terrier"
    def bark():
        print("Wuuofff")

#creating bostons
iggy = Dog()
nacho = Dog()
print(nacho.breed)
Dog.breed = "Chihuahua"
nacho.breed="Boston"
print(nacho.breed)
nacho.age = 5
print(nacho.age)
kichi = Dog()