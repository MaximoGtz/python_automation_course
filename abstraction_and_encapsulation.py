class Customer:
    def __init__(self, name):
        self.name = name
        self.books = []

    def watch_books(self):
        if len(self.books) == 0:
            print("You dont have any books.")
        else:
            print("Your books", len(self.books), ":")
            for book in self.books:
                book.print_info()
    
    def get_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

    def return_book(self, book_name):
        for i, book in enumerate(self.books):
            if book_name == book.get_name():
                self.books.pop(i)
                print(book.get_name(), " has been returned")
                return  # Exit the method after successful return
        print("Customer doesn't have the book: ", book_name)


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []
        self.books_quantity = 0

    def add_books(self, books_array):
        self.books = books_array
    
    def get_aviable_books(self):
        counter=0
        print("These are the aviable books(",len(self.books),"): ")
        for book in self.books:
            book.print_info()

    def remove_book(self, book):
        counter = 0
        for book in self.books:
            if book == self.books[counter]:
                self.books.pop(counter)
    def add_book(self, book):
        self.books.append(book)
    
    def return_book(self, customer, book_name):
        find_book = False
        counter = 0
        for book in customer.get_books():
            if book_name == book.get_name():
                print("Book found!")
                customer.return_book(book_name)
                self.add_book(book)
                find_book == True
                break
        
           
            
    def borrow_book(self, customer, book_name):
        got_the_book = False
        for book in self.books:
            if book.name == book_name:
                customer.get_book(book)
                got_the_book = True
                self.remove_book(book)
                print("Book borrowed!")
                break
        if got_the_book == False:
            print("We don't have that book right now, sorry")                    
        

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def print_info(self):
        print("Name:", self.name, " Author:", self.author, " Year:", self.year)
    
    def get_name(self):
        return self.name
    
#FILL LIBRARY
book1 = Book("The Divine Comedy", "Dante Alighieri", 1320)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book4 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", 1967)
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book6 = Book("Beloved", "Toni Morrison", 1987)
book7 = Book("1984", "George Orwell", 1949)
book8 = Book("Things Fall Apart", "Chinua Achebe", 1958)
book9 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book10 = Book("Invisible Man", "Ralph Ellison", 1952)
books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]
library = Library()
library.add_books(books)
customer1 = Customer("Maximo")
while True:
    print("What would you like to do?")
    print("1. Watch avaiable books")
    print("2. Watch your books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")
    user_choice = int(input())
    if user_choice == 1:
        library.get_aviable_books()
    elif user_choice == 2:
        customer1.watch_books()
    elif user_choice == 3:
        print("Wich book do you want?")
        book_text = input()
        library.borrow_book(customer1, book_text)
    elif user_choice == 4:
        print("Wich book do you want to return?")
        book_text = input()
        library.return_book(customer1, book_text)
    elif user_choice == 5:
        quit()
