# File: /draft.py

from models import *
from dao import *

class SalesController:
    def register(self, nameProduct, seller, buyer, quantity_sold):
        stockdao = StockDao.read()

        stock_temp = []
        product_exist = False
        quantity_stock = False

        for i1 in stockdao:
            if product_exist == False:
                if i1.product.name == nameProduct:
                    product_exist == True
                    if i1.quantity >= quantity_sold:
                        quantity_stock == True
                        i1.quantity = int(i1.quantity) - int(quantity_sold)

                        solded = SalesModel(ProductModel(i1.product.name,
                                                         i1.product.price,
                                                         i1.product.category),
                                                         seller, buyer, quantity_sold)
                        SalesDao.save(solded)
                        purchase_value = int(quantity_sold) * float(i1.product.price)

            stock_temp.append([ProductModel(i1.product.name,
                                         i1.product.price,
                                         i1.product.category),
                                         i1.quantity])
            file = open('hd_stock.txt', 'w')
            file.write('')

            for i2 in stock_temp:
                with open('hd)stock.txt', 'a') as file:
                    file.writelines(i2[0].name + '|' +
                                    i2[0].price + '|' +
                                    i2[0].category + '|' +
                                    str(i2[1]))
                    file.writelines('\n')

            if product_exist == False:
                print('This product does not exist.')
                return None
            elif not quantity_stock:
                print('The quantity sold is not in stock.')
                return None
            else:
                print('Sale completed successfully.')
                return purchase_value


            