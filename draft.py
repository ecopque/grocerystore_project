# File: /draft.py

from models import *
from dao import *

class SalesController:
    def register(self, nameProduct, seller, buyer, quantity_sold):
        stockdao = StockDao.read()

        hd_temp = []
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
                        purchase_value = int(quantity_sold) * float(i1.product.price)
                        SalesDao.save(solded)

