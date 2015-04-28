class Book:
    def __init__(self, bookName, bookId):
        self.name = bookName
        self.id = bookId

    def __str__(self):
        return self.name + " :: " + str(self.id)

class Customer:
    def __init__(self, name):
        self.booksRented = []
        self.name = name

    def rentBook(self, book):
        self.booksRented.append(book)

    def returnBook(self, book):
        self.booksRented.remove(book)

    def __str__(self):
        return self.name

class LibraryMapper:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        _print("added book [" + str(book) + "]")

    def giveBook(self, book, customer):
        customer.rentBook(book)
        self.books.remove(book)
        _print("gave [" + str(book) + "] to [" + str(customer) + "]")

    def returnBook(self, book, customer):
        customer.returnBook(book)
        _print("return [" + str(book) + "] from [" + str(customer) + "]")
        self.addBook(book)

    def __str__(self):
        s = "\nLIBRARY STORE\n"
        for b in range(len(self.books)):
            s = s + "::" + self.books[b].name + "::\n"
        return s

def main():
    # make mapper
    lib = LibraryMapper()
    # make all the customers
    cus1 = Customer("ethan")
    cus2 = Customer("matt")
    cus3 = Customer("zach")
    cus4 = Customer("kevin")
    # make all the books
    b1 = Book("Harry Pot-head", 1)
    b2 = Book("Lord of the Carnival Ring Game", 2)
    b3 = Book("Trapped in the Wordrobe", 3)
    b4 = Book("Hitchhikers guide to Narnia", 4)
    # add books to lib
    lib.addBook(b1)
    lib.addBook(b2)
    lib.addBook(b3)
    lib.addBook(b4)
    _print(lib)
    # give books to people
    lib.giveBook(b1,cus1)
    lib.giveBook(b4,cus3)
    lib.giveBook(b2,cus4)
    _print(lib)
    # return books to lib
    lib.returnBook(b4,cus3)
    lib.returnBook(b2,cus4)
    _print(lib)

# shouldn't matter which version of python it runs
def _print(string):
    try:
        print string
    except SyntaxError:
        print(string)

if __name__ == "__main__": main()
