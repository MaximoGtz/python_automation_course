#Check if an employee has achieved his weekly target or not
class Employee:
    name = "Ben"
    designation = "Sales executive"
    sales_made_this_week = 6
    def has_achieved_target(self):
        if self.sales_made_this_week >= 5:
            return "Target has been achieved"
        else:
            return "Target has not been achieved"
employee_one = Employee()
print(employee_one.name)
print(employee_one.has_achieved_target())
employee_two = Employee()


