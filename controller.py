# FILE: /controller.py

from models import *
from dao import *

class CategoryController:
    def register(self, newcategory):
        categorydao_read = CategoryDao.read()
        
        exists_flag = False
        for i in categorydao_read:
            if i.category == newcategory: #11:
                exists_flag = True
        
        if not exists_flag:
            CategoryDao.save(newcategory)
            print('Category registered successfully.')
        else:
            print('The category you want to register already exists.')

    def remove(self, removecategory):
        categorydao_read = CategoryDao.read()

        # cat = list(filter(lambda read_category: read_category.category == removecategory, read_category))
        cat = []
        for i in categorydao_read:
            if i.category == removecategory:
                cat.append(i)
    
        if len(cat) == 0:
            print('The category you want to remove does not exist.')
        
        else:
            for i in range(len(categorydao_read) -1, -1, -1): #12:
                if categorydao_read[i].category == removecategory:
                    del categorydao_read[i]
            print('Category removed successfully.')
        #TODO: Put uncategorized in stock
            with open('hd_category.txt', 'w') as file:
                    for i in categorydao_read:
                        file.writelines(i.category)
                        file.writelines('\n')
    def change(self, changecategory, newcategory):
        categorydao_read = CategoryDao.read()

        # cat1 = list(filter(lambda read_category: read_category.category == changecategory, read_category))
        cat1 = []
        for i in categorydao_read:
            if i.category == changecategory:
                cat1.append(i)
        
        if len(cat1) > 0:
            # cat2 = list(filter(lambda read_category: read_category.category == newcategory, read_category))
            cat2 = []
            for i in categorydao_read:
                if i.category == newcategory:
                    cat2.append(i)
            
            if len(cat2) == 0:
                # read_category = list(map(lambda read_category: CategoryModel(newcategory) if (read_category.category == changecategory) else (read_category), read_category))
                for i in range(len(categorydao_read)):
                    if categorydao_read[i].category == changecategory:
                        categorydao_read[i].category = newcategory
                print(f"Category '{changecategory}' changed to '{newcategory}' successfully.")
                #TODO: Change stock category.
            else:
                print(f"The category '{newcategory}' already exists.")
        else:
           print(f"The category '{newcategory}' you want to change does not exist.")

        with open('hd_category.txt', 'w') as file:
            for i in categorydao_read:
                file.writelines(i.category)
                file.writelines('\n')

    def showcategory(self):
        categorydao_read = CategoryDao.read()

        if len(categorydao_read) == 0:
            print('There are no registered categories.')
            return 0
        
        for i in categorydao_read:
            print(f'Categorie: {i.category}.')
    
class StockController:
    def register(self, name, price, category, quantity):
        stockdao_read = StockDao.read()
        categorydao_read = CategoryDao.read()
    


# registration_test = CategoryController()
# registration_test.register('Cold cuts') #10:

# remove_test = CategoryController()
# remove_test.remove('Z')

# change_category = CategoryController()
# change_category.change('Vegetables', 'Naturals')

show_category = CategoryController()
show_category.showcategory()