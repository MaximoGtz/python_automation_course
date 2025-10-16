class Animal:
    def employeeDetails(self):
        self.name = "Raccoon"


    #This is a static method, you don't need to pass any arguments to it
    @staticmethod
    def sayHi():
        print("Hi, I'm an animal")
nacho = Animal()
nacho.sayHi()