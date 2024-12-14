# File: /temp.py

from datetime import datetime

class CategoryModel:
    def __init__(self, category):
        self.category = category

class ProductModel:
    def __init__(self, name, price, category: CategoryModel): # ****
        self.name = name
        self.price = price
        self.category = category

class StockModel:
    def __init__(self, product: ProductModel, quantity):
        self.product = product
        self.quantity = quantity

class SalesModel:
    def __init__(self, items_sold, product, seller, buyer, quantity_sold, sale, date = datetime.now()):
        ...

########################
class CategoryDao:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')
    
    @classmethod
    def read(cls):
        with open('category.txt', 'r') as file:
            cls.category = file.readlines()
        print(cls.category)

        cat = []
        for i in cls.category:
            cat.append(CategoryModel(i))

CategoryDao.save('Hugo')
CategoryDao.read()

########################
