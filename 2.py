# Design a class Book with private attributes title, author, and price. Create methods to set and get the values of these attributes. Ensure that the price cannot be set below a certain value (e.g., 10).


class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def getTitle(self):
        return self.__title
    
    def setTitle(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__title = value

    def getAuthor(self):
        return self.__author
    
    def setAuthor(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__author = value

    def getPrice(self):
        return self.__price
    
    def setPrice(self, value):
        certain_val = 10
        if value < certain_val:
            raise ValueError(f"Price can't be less than {certain_val}.")
        self.__price = value

ob = Book("Harry Potter", "J. K. Rowling", 50)
print(ob.getPrice())
ob.setPrice(10)
print(ob.getPrice())
ob.setPrice(5)
print(ob.getPrice())