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
@classmethod
    def read(cls):
        with open('hd_stock.txt', 'a') as file:
            cls.stock = file.readlines()

        for i in range(len(cls.stock)):
            cls.stock[i] = cls.stock[i].replace('\n', '')
        print(cls.stock)

        for i in range(len(cls.stock)):
            cls.stock[i] = cls.stock[i].split('|')
        print(cls.stock)

        stock_hd = []
        for i in cls.stock:
            stock_hd.append(StockModel(ProductModel(i[0], i[1], i[2]), i[3]))
        return stock_hd
# Laços for é elegante, ao contrário de algumas funções e list comprehension.

from model import *
from dao import *

class RegisterController:
    def register(self, newcategory):
        read_categorydao = CategoryDao.read()

        exists_flag = False
        for i in read_categorydao:
            if i.category == newcategory:
                exists_flag = True
        
        if not exists_flag:
            CategoryDao.save(newcategory)
            print('Category registered successfully.')

        else:
            print('Fiodeu!')