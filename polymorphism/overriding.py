class Employee:
    def set_number_of_working_hours(self):
        self.number_of_working_hours = 40

    def get_number_of_working_hours(self):
        return self.number_of_working_hours 
employee1 = Employee()
employee1.set_number_of_working_hours()
print("Number of working hours of employee: ",)


#You can override functions when you inherit, but also, you can acceed to the function of the father if you need to, using the super() method


class GovermentSale():
    def calculate_extras():
        print("Hellos")
