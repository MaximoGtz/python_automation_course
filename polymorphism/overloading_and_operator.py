class Square():
    def __init__(self,side):
        self.side = side
    #Lets overload the method to make adding method
    def __add__(squareOne,squareTwo):
        return ((4*squareOne.side) + (4*squareTwo.side))
    def __sub__(squareOne, squareTwo):
        return ((4*squareOne.side) - (4*squareTwo.side))
    def __mul__(squareOne, squareTwo):
        return ((4*squareOne.side) * (4*squareTwo.side))
    def __floordiv__(squareOne, squareTwo):
        return ((4*squareOne.side) // (4*squareTwo.side))
    def __truediv__(squareOne, squareTwo):
        return ((4*squareOne.side) / (4*squareTwo.side))
    def __mod__(squareOne, squareTwo):
        return ((4*squareOne.side) / (4*squareTwo.side))
    
square1 = Square(3)
square2 = Square(5)
#Now the sum method is working as we expected, we sum all of the sides of te squares and add return the information
#We can also overload the other operators such as "-", "/", "*" and so on...
print("Sum of sides of both of the squares = ", square1 + square2)
print("Substraction of sides of both of the squares = ", square2 - square1)
print("Multiplication of sides of both of the squares = ", square2 * square1)
print("Floor division of sides of both of the squares = ", square2 // square1)
print("True division of sides of both of the squares = ", square2 / square1)
#__add__(self, other): Implements behavior for the + operator (addition).
#__sub__(self, other): Implements behavior for the - operator (subtraction).
#__mul__(self, other): Implements behavior for the * operator (multiplication).
#__floordiv__(self, other): Implements behavior for the // operator (floor division).
#__truediv__(self, other): Implements behavior for the / operator (true division).
#__mod__(self, other): Implements behavior for the % operator (modulus).
#__divmod__(self, other): Implements behavior for the divmod() function.
#__pow__(self, other): Implements behavior for the ** operator (exponentiation).
#__lshift__(self, other): Implements behavior for the << operator (left bitwise shift).
#__rshift__(self, other): Implements behavior for the >> operator (right bitwise shift).
#__and__(self, other): Implements behavior for the & operator (bitwise and).
#__or__(self, other): Implements behavior for the | operator (bitwise or).
#__xor__(self, other): Implements behavior for the ^ operator (bitwise xor).
#__invert__(self): Implements behavior for bitwise NOT using the ~ operator.
#__neg__(self): Implements behavior for negation using the - operator.
#__pos__(self): Implements behavior for unary positive using the + operator.
# FOR MORE INFO VISIT:
# https://www.geeksforgeeks.org/python/dunder-magic-methods-python/