# File: /dao.py
# Data Access Object

from models import *

class CategoryDao:
    @classmethod
    def save(cls, category):
        with open('hd_category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_category.txt', 'r') as file:
            cls.category = file.readlines()
        
        # cls.category = list(map(lambda x: x.replace('\n', ''), cls.category)) #2:
        for i in range(len(cls.category)):
            cls.category[i] = cls.category[i].replace('\n', '')
        print(cls.category)

        cat = [] #1:
        for i in cls.category: #1:
            cat.append(CategoryModel(i)) #1:
        return cat

CategoryDao.save('Fruits')
CategoryDao.save('Vegetables')
CategoryDao.save('Legumes')
CategoryDao.read() #4:

class SalesDao:
    @classmethod
    def save(cls, sale: SalesModel):
        with open('hd_sale.txt', 'a') as file:
            file.writelines(sale.items_sold.name + '|' + 
                            str(sale.items_sold.price) + '|' + 
                            sale.items_sold.category + '|' + 
                            sale.seller + '|' + 
                            sale.buyer + '|' + 
                            str(sale.quantity_sold) + '|' + 
                            sale.date) #3:
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_sale.txt', 'r') as file:
            cls.sale = file.readlines()

        for i in range(len(cls.sale)):
            cls.sale[i] = cls.sale[i].replace('\n', '')
        print(cls.sale) #5:

        for i in range(len(cls.sale)):
            cls.sale[i] = cls.sale[i].split('|')
        print(cls.sale) #6:

        sale_hd = []
        for i in cls.sale:
            sale_hd.append(SalesModel(ProductModel(i[0], float(i[1]), i[2]), i[3], i[4], int(i[5]), i[6]))
        return sale_hd

class StockDao:
    @classmethod
    def save(cls, product: ProductModel, quantity):
        with open('hd_stock.txt', 'a') as file:
            file.writelines(product.name + '|' + product.price + '|' + product.category + '|' + str(quantity))
            file.writelines('\n')

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






p1_product = ProductModel('bean', 7, 'Legumes')
p1_sale = SalesModel(p1_product, 'Edson', 'Théo', 3)
SalesDao.save(p1_sale)
SalesDao.read() # (#5, #6)

x = SalesDao.read()
print(x[0].buyer) #7:
print(x[0].items_sold.name) #8:
print(x[0].items_sold.price) #9:


# Edson Copque | https://linktr.ee/edsoncopque