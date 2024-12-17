# FILE: /controller.py

from models import *
from dao import *

class CategoryController:
    def register(self, newcategory):
        read_categorydao = CategoryDao.read()
        
        exists_flag = False
        for i in read_categorydao:
            if i.category == newcategory: #11:
                exists_flag = True
        
        if not exists_flag:
            CategoryDao.save(newcategory)
            print('Category registered successfully.')
        else:
            print('The category you want to register already exists.')

registration_test = CategoryController()
registration_test.register('Cold cuts') #10: