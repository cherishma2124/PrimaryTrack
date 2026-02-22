from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

  
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

 
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty!")
        self.__name = name

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = price

    def set_stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be negative!")
        self.__stock = stock

    def add_stock(self, qty):
        if qty <= 0:
            raise ValueError("Quantity must be > 0")
        self.__stock += qty

    def remove_stock(self, qty):
        if qty <= 0:
            raise ValueError("Quantity must be > 0")
        if qty > self.__stock:
            raise ValueError("Not enough stock!")
        self.__stock -= qty

    @abstractmethod
    def to_dict(self):
        pass

    def __str__(self):
        return f"{self.__product_id} | {self.__name} | ₹{self.__price} | Stock: {self.__stock}"


class Electronics(Product):
    def __init__(self, product_id, name, price, stock, brand, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.__brand = brand
        self.__warranty_years = warranty_years

    def to_dict(self):
        return {
            "type": "Electronics",
            "id": self.get_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "brand": self.__brand,
            "warranty_years": self.__warranty_years
        }

    def __str__(self):
        return super().__str__() + f" | Brand: {self.__brand} | Warranty: {self.__warranty_years} yrs"


class Grocery(Product):
    def __init__(self, product_id, name, price, stock, expiry_date):
        super().__init__(product_id, name, price, stock)
        self.__expiry_date = expiry_date

    def to_dict(self):
        return {
            "type": "Grocery",
            "id": self.get_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "expiry_date": self.__expiry_date
        }

    def __str__(self):
        return super().__str__() + f" | Expiry: {self.__expiry_date}"