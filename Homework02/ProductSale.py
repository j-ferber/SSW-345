# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None

    def __init__(self, sale: Sale, init: int = 0):
        self.__lastSale = sale
        self.__inventory = init

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    def __getitem__(self, item):
        return self
    
    def getInventory(self):
        return self.__inventory
    
    def setInventory(self, value):
        self.__inventory = value

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product]):  #, saleNumber: int = 1):
        Sale.__saleTimes +=1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes
        for index, product in enumerate(product):
            product[index].setLastSale(self)
            product[index].setInventory(product[index].getInventory() - 1)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, init=10)
productTwo = Product(sale=None, init=5)
print(f"Inventory:\nProduct One: {productOne.getInventory()}\nProduct Two: {productTwo.getInventory()}\n")

saleOne = Sale([productOne, productTwo])
print(f"After Product One and Product Two Sale Inventory:\nProduct One: {productOne.getInventory()}\nProduct Two: {productTwo.getInventory()}\n")

saleTwo = Sale([productOne])
print(f"After Product One Sale Inventory:\nProduct One: {productOne.getInventory()}\nProduct Two: {productTwo.getInventory()}\n")

saleThree = Sale([productTwo])
print(f"After Product Two Sale Inventory:\nProduct One: {productOne.getInventory()}\nProduct Two: {productTwo.getInventory()}\n")

print(f"{productOne.getLastSale.getSaleNumber}, {productTwo.getLastSale.getSaleNumber}")
