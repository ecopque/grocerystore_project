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