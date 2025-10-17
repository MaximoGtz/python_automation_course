# This doesn't mean you cant access to this variables along the execution.
#THis only has meaning for other developers

#As you know, they are 3 levels of protection into the variables.
# Public => member_name
# Protected => _member_name
# Private => __member_names

class Car:
    #public
    number_of_wheels = 4
    #protected
    _color = "Black"
    #private
    __year_of_manufacture = 2017



car = Car()
#You can always get the public attributes
print("Public attribute: ", car.number_of_wheels)
#It is the same as the public but for convention, you know as a developer that you shouldn't use it outside of the class
print("Protected attribute: ", car._color)
#You can't acces directly writing the attributes as a protected or private one. But it doesn't mean you can't access to it. You just need to use another syntax.
#WRONG
#ALSO THE DEVELOPER DOESN'T WANT YOU TO USE IT OUTSIDE OF THE CLASS
#print("Private attribute: ", car.__year_of_manufacture)
#But if you don't care about it, you can have access to it like this
print(car._Car__year_of_manufacture)
#This happens because name mangling is being done to your attribute.
#What is is happening is that this variable is being prepended.