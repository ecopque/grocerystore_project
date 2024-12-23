# File: /draft.py

from models import *
from dao import *

class SalesController:
    def report(self):
        salesdao_read = SalesDao.read()
        products = []

        for i1 in salesdao_read:
            name = i1.items_sold.name
            quantity = i1.quantity_sold

            size = []
            for i2 in products:
                if i2['product'] == name:
                    size.append(i2)

            if len(size) > 0:
                for i3 in products:
                    if i3['product'] == name:
                        i3['quantity'] = int(i3['quantity']) + int(quantity)
            else:
               products.append({'product': name, 'quantity': int(quantity)})
        
        ordered = products.copy()
        for i4 in range(len(ordered)):
            for j4 in range(i4 + 1, len)