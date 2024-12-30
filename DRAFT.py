# File: /draft.py

from models import *
from dao import *


class CategoryController:
    def remove(self, removecategory):
        ...

        salesdao_read = StockDao.read()

        for i4 in range(len(salesdao_read)):
            if salesdao_read[i4].product.category == removecategory:
                salesdao_read[i4] = StockModel(ProductModel(
                    salesdao_read[i4].product.name,
                    salesdao_read[i4].product.price,
                    'uncategorized'),
                    salesdao_read[i4].quantity)