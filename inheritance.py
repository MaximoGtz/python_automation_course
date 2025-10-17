class Apple:
    manufacturer = "Apple Inc."
    contact_website = "www.apple.com/contact"
    def contact_details(self):
        print("To contact us, log on to", self.contact_website)

#In order to inherit the attributes and data from the father class, you should do the next. Just put apple into the parenthesis
class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2018
    def manufacture_details(self):
        print("This MacBook was manufactured in the year {} by {}".format(self.year_of_manufacture, self.manufacturer))
#INTERESTING CONCATENATION OF ELEMENTS
#You can concat elements by just adding {} into the string and then assign values using the function .format() to the string. Then you add the values into the parenthesis

mac_book = MacBook()
mac_book.manufacture_details()