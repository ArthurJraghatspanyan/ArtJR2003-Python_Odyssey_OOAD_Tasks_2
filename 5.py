# Design a class Product with private attributes product_id, product_name, and quantity_in_stock. Implement methods to set and get the values of these attributes and to adjust the quantity_in_stock (e.g., adding stock or reducing stock).

class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def getProductID(self):
        return self.__product_id
    def setProductID(self, value):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__product_id = value

    def getProductName(self):
        return self.__product_name
    def setProductName(self, value):
        if not isinstance(value, str):
            raise TypeError("Type must be str.")
        self.__product_name = value

    def getQuantityInStock(self):
        print(f"Total quantity in stock: {self.__quantity_in_stock}")
    def setQuantityInStock(self, value):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__quantity_in_stock = value

    def adding_stock(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__quantity_in_stock += value

    def removing_stock(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Type must be int.")
        self.__quantity_in_stock -= value

product = Product(1, "Notebook", 3)
product.getQuantityInStock()
product.adding_stock(3)
product.getQuantityInStock()
product.removing_stock(2)
product.getQuantityInStock()
product.adding_stock(100)
product.getQuantityInStock()