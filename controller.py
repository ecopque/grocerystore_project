# FILE: /controller.py

from models import *
from dao import *

class CategoryController:
    def register_category(self, newcategory):
        exists = False
        read_categorydao = CategoryDao.read()
        for i in read_categorydao:
            if i.category == newcategory: #11:
                exists = True
        if not exists:
            CategoryDao.save(newcategory)
            print('Category registered successfully.')
        else:
            print('The category you want to register already exists.')

registration_test = CategoryController()
registration_test.register_category('Cold cuts') #10: 