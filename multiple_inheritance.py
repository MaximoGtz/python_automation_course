#When you inherit from two classes, you take both, methods and attributes from both classes.
#If you have the same attribute in both classes, the attribute the son class inherits is the attributes that came first. Lets take a look in an example

class Mom:
    last_name = "Iñiguez"
class Dad:
    last_name = "Gutierrez"

class Son(Dad, Mom):
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print("Your name is {} {}".format(self.name, self.last_name))
max = Son("Maximo")
max.print_name()
#as you can see, Maximo inherits the last name from the dad because it was put first in the heritance.
