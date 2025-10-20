class Employee:
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 40

    def get_number_of_working_hours(self):
        return self.number_of_working_hours 
    
class Trainee(Employee):
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 45

    #You can override functions when you inherit, but also, you can acceed to the function of the father if you need to, using the super() method
    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours()

trainee1 = Trainee()
trainee1.set_number_of_working_hours()
print("Number of working hours from the employee:", trainee1.get_number_of_working_hours())
trainee1.reset_number_of_working_hours()
print("Number of working hours from the employee:", trainee1.get_number_of_working_hours())

#employee1 = Employee()
#employee1.set_number_of_working_hours()
#trainee1.set_number_of_working_hours()
#print("Number of working hours from the employee:", employee1.get_number_of_working_hours())
#print("Number of working hours from the trainee:", trainee1.get_number_of_working_hours())
#



class GovermentSale():
    __cost = 0.16
    def calculate_extras():
        print("Hellos")
