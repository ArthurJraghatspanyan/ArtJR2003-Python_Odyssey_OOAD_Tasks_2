# Design a class ShoppingCart that encapsulates a private list of items (items). Implement methods to add an item, remove an item, and display the total number of items in the cart. Each item should have a name and price.

# NOT COMPLETED YET

class ShoppingCart:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__items = []
        self.di = {}

        self.di[self.__name] = self.__price
        self.__items.append(self.di)

    def setName(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__name = value

    def getName(self):
        return self.__name

    def setPrice(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int.")
        self.__price = value

    def getPrice(self):
        return self.__price
    
    def addItem(self):
        self.di[self.getName()] = self.getPrice()

    def removeItem(self, value):
        if value not in self.di:
            raise ValueError("This value doesn't exits.")
        self.di.pop(value)

    def numberofItems(self):
        print(self.__items)
        print(f"Total number of items is {len(self.di)}")

shoppingcart = ShoppingCart("Banana", 300)
shoppingcart.numberofItems()
shoppingcart.setName("Apple")
shoppingcart.setPrice(500)
shoppingcart.addItem()
shoppingcart.numberofItems()
shoppingcart.removeItem("Apple")
shoppingcart.numberofItems()
shoppingcart.setName("Pineapple")
shoppingcart.setPrice(600)
shoppingcart.addItem()
shoppingcart.numberofItems()