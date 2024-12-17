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

    def remove(self, removecategory):
        read_category = CategoryDao.read()

        # cat = list(filter(lambda x: x.category == removecategory, x))
        cat = []
        for i in read_category:
            if i.category == removecategory:
                cat.append(i)
    
        if len(cat) <= 0:
            print('The category you want to remove does not exist.')
        else:
            for i in range(len(read_category)):
                if read_category[i] == removecategory:
                    del read_category[i]
                    break
                print('Category removed successfully.')
               
                with open('hd_category.txt', 'w') as file:
                    for i in read_category:
                        file.writelines(i.category)
                        file.writelines('\n')


registration_test = CategoryController()
registration_test.register('Cold cuts') #10:

