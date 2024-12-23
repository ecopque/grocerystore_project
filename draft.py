# File: /draft.py

from models import *
from dao import *

class StockController:
    def show(self):
        stockdao_read = StockDao.read()

        if len(stockdao_read) == 0:
            print('Empty stock.')
        
        else:
            print('PRODUCTS:')
            for i1 in stockdao_read:
                print(f'Name: {i1.product.name}, Price: {i1.product.price}, Category: {i1.product.category}, Quantity: {i1.quantity}')


            