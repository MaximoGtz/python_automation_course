import math, os
#From abstract base class import Abstract Base Clas and abstract method wich is a decorator
from abc import ABC, abstractmethod
class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        print("Area of the square: ",self.side * 4 )

    
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = math.pi * (self.radius * self.radius)
        print("Area of the circle: ", area)

circle = Circle(4)
circle.area()
square = Square(5)
square.area()
os.system('cls') 
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
# Error    
#car = Vehicle()
class Car(Vehicle):
    @staticmethod
    def laravel():
        print("Hello world!")

    def go(self):
        print("You are driving that car.")
    def stop(self):
        print("You stopped the car.")
class Motorcycle(Vehicle):
    def go(self):
        print("You are driving that motorcycle.")
    def stop(self):
        print("You stopped the motorcycle.")
car1 = Car()

car1.go()
car1.stop()
motorcycle1 = Motorcycle()
motorcycle1.go()
motorcycle1.stop()