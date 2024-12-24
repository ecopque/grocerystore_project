# File: /draft.py

from models import *
from dao import *
from datetime import datetime

class SalesController:
    def show(self, startDate, endDate):
        salesdao_read = SalesDao.read()
        startdate = datetime.strptime(startDate, '%d/%m/%Y')
        enddate = datetime.strptime(endDate, '%d/%m/%Y')

        selected_sales = []
        for i1 in salesdao_read:
            sale_date = datetime.strptime(i1.date, '%d/%m/%Y')
            if sale_date >= startdate and sale_date <= enddate:
                selected_sales.append(i1)

        count_var = 1
        total = 0

        for i2 in selected_sales:
            print(f'===== SALE [{count_var}] =====')
            print(f'Name: {i2.items_sold.name}\n'
            f'')

        total = int(i2.items_sold.price) * int(i2.quantity_sold)