# FILE: /controller.py

from models import *
from dao import *

class CategoryController:
    def register(self, newcategory):
        categorydao_read = CategoryDao.read()
        
        exists_flag = False
        for i1 in categorydao_read:
            if i1.category == newcategory: #11:
                exists_flag = True
        
        if not exists_flag:
            CategoryDao.save(newcategory)
            print('Category registered successfully.')
        else:
            print('The category you want to register already exists.')

    def remove(self, removecategory):
        categorydao_read = CategoryDao.read()

        # hd_compare_cat = list(filter(lambda read_category: read_category.category == removecategory, read_category))

        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == removecategory:
                hd_compare_cat.append(i1)
    
        if len(hd_compare_cat) == 0:
            print('The category you want to remove does not exist.')
        
        else:
            for i2 in range(len(categorydao_read) -1, -1, -1): #12:
                if categorydao_read[i2].category == removecategory:
                    del categorydao_read[i2]
            print('Category removed successfully.')
        #TODO: Put uncategorized in stock
            with open('hd_category.txt', 'w') as file:
                    for i2 in categorydao_read:
                        file.writelines(i2.category)
                        file.writelines('\n')
    def change(self, changecategory, newcategory):
        categorydao_read = CategoryDao.read()

        # hd_compare_cat = list(filter(lambda read_category: read_category.category == changecategory, read_category))
        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == changecategory:
                hd_compare_cat.append(i1)
        
        if len(hd_compare_cat) > 0:

            # hd_compare_cat2 = list(filter(lambda read_category: read_category.category == newcategory, read_category))
            
            hd_compare_cat2 = []
            for i2 in categorydao_read:
                if i2.category == newcategory:
                    hd_compare_cat2.append(i2)
            
            if len(hd_compare_cat2) == 0:

                # read_category = list(map(lambda read_category: CategoryModel(newcategory) if (read_category.category == changecategory) else (read_category), read_category))
                
                for i3 in range(len(categorydao_read)):
                    if categorydao_read[i3].category == changecategory:
                        categorydao_read[i3].category = newcategory
                print(f"Category '{changecategory}' changed to '{newcategory}' successfully.")
                #TODO: Change stock category.
            else:
                print(f"The category '{newcategory}' already exists.")
        else:
           print(f"The category '{newcategory}' you want to change does not exist.")

        with open('hd_category.txt', 'w') as file:
            for i4 in categorydao_read:
                file.writelines(i4.category)
                file.writelines('\n')

    def show(self):
        categorydao_read = CategoryDao.read()

        if len(categorydao_read) == 0:
            print('There are no registered categories.')
            return 0
        
        for i1 in categorydao_read:
            print(f'Categorie: {i1.category}.')
    
class StockController:
    def register(self, name, price, category, quantity):
        categorydao_read = CategoryDao.read()
        stockdao_read = StockDao.read()
        
        # hd_compare_cat = list(filter(lambda stockdao_read: stockdao_read.category == category, categorydao_read))
        # hd_compare_name = list(filter(lambda stockdao_read: stockdao_read.product.name == name, stockdao_read))

        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == category:
                hd_compare_cat.append(i1)

        hd_compare_name = []
        for i2 in stockdao_read:
            if i2.product.name == name:
                hd_compare_name.append(i2)

        if len(hd_compare_cat) > 0:
            if len(hd_compare_name) == 0:
                product = ProductModel(name, price, category)
                StockDao.save(product, quantity)
                print('Product registered successfully.')
            else:
                print('Product already in stock.')
        else:
            print('Category does not exist.')

    def remove(self, name):
        stockdao_read = StockDao.read()

        hd_compare_name = []
        for i1 in stockdao_read:
            if i1.product.name == name:
                hd_compare_name.append(i1)

        if len(hd_compare_name) > 0:
            for i2 in range(len(stockdao_read)):
                if stockdao_read[i2].product.name == name:
                    del stockdao_read[i2]
                    break
            print('Product removed successfully.')
            
        else:
            print('The product you want to remove does not exist.')

        with open('hd_stock.txt', 'w') as file:
            for i3 in stockdao_read:
                file.writelines(i3.product.name + '|' + 
                            str(i3.product.price) + '|' + 
                            i3.product.category + '|' + 
                            str(i3.quantity))
                file.writelines('\n')

    def change(self, nameOld, nameNew, priceNew, categoryNew, quantityNew):
        categorydao_read = CategoryDao.read()
        stockdao_read = StockDao.read()

        # hd_compare_cat = list(filter(lambda x: x.category == categoryNew, categorydao_read))
        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == categoryNew:
                hd_compare_cat.append(i1)

        if len(hd_compare_cat) > 0:
            # hd_compare_name = list(filter(lambda x: x.product.name == nameOld, stockdao_read))
            hd_compare_name = []
            for i2 in stockdao_read:
                if i2.product.name == nameOld:
                    hd_compare_name.append(i2)
            
            if len(hd_compare_name) > 0:
                # hd_compare_name = list(filter(lambda x: x.product.name == nameNew, stockdao_read))
                hd_compare_name = []
                for i3 in stockdao_read:
                    if i3.product.name == nameNew:
                        hd_compare_name.append(i3)

                if len(hd_compare_name) == 0:
                    # stockdao_read = list(map(lambda x: StockModel(ProductModel(nameNew, priceNew, categoryNew), quantityNew) if(x.product.name == nameOld) else (x), stockdao_read))
                    for i4 in range(len(stockdao_read)):
                        if stockdao_read[i4].product.name == nameOld:
                            stockdao_read[i4] = StockModel(ProductModel(nameNew, priceNew, categoryNew), quantityNew)
                    print('Product changed successfully.')
                else:
                    print('Product already registered.')
            else:
                print('The product you want to change does not exist.')

            with open('hd_stock.txt', 'w') as file:
                for i5 in stockdao_read:
                    file.writelines(i5.product.name + '|' + 
                            str(i5.product.price) + '|' + 
                            i5.product.category + '|' + 
                            str(i5.quantity))
                    file.writelines('\n')
        else:
            print('The category provided does not exist.')

    def show(self):
        stockdao_read = StockDao.read()
        
        if len(stockdao_read) == 0:
            print('Empty stock.')
        
        else:
            print('PRODUCTS: ')
            for i1 in stockdao_read:
                print(f'Name: {i1.product.name}, Price: {i1.product.price}, Category: {i1.product.category}, Quantity: {i1.quantity}.')

#TODO: Launch on mind map
class SalesController:
    def register(self, nameProduct, seller, buyer, quantity_sold):
        stockdao = StockDao.read()
        
        stock_temp = []
        product_exist = False #14:
        quantity_stock = False #13:

        for i1 in stockdao:
            if product_exist == False:
                if i1.product.name == nameProduct:
                    product_exist = True
                    if i1.quantity >= quantity_sold:
                        quantity_stock = True
                        i1.quantity = int(i1.quantity) - int(quantity_sold)
                        
                        # see StockDao.read()
                        # i1 = StockModel instance.
                        # i1.product = ProductModel instance.
                        solded = SalesModel(ProductModel(i1.product.name, 
                                                         i1.product.price, 
                                                         i1.product.category), 
                                                         seller, buyer, quantity_sold)
                        SalesDao.save(solded)
                        purchase_value = int(quantity_sold) * float(i1.product.price)

            stock_temp.append([ProductModel(i1.product.name, 
                                   i1.product.price, 
                                   i1.product.category), 
                                   i1.quantity]) #16:
            file = open('hd_stock.txt', 'w')
            file.write('')

            # [[Product('name', 'price', 'category'), quantity]]
            for i2 in stock_temp:
                with open('hd_stock.txt', 'a') as file:
                    file.writelines(i2[0].name + '|' + 
                                    i2[0].price + '|' + 
                                    i2[0].category + '|' + 
                                    str(i2[1]))
                    file.writelines('\n')

            if product_exist == False:
                print('The product does not exist.')
                return None
            elif not quantity_stock: #15: #17:
                print('The quantity sold is not in stock.')
                return None
            else:
                print('Sale completed successfully.')
                return purchase_value





                
# registration_test = CategoryController()
# registration_test.register('Cold cuts') #10:

# remove_test = CategoryController()
# remove_test.remove('Z')

# change_category = CategoryController()
# change_category.change('Vegetables', 'Naturals')

# show_category = CategoryController()
# show_category.showcategory()

# show_register = StockController()
# show_register.register('banana', 15, 'Fruits', 100)

# remove_stockcontroller = StockController()
# remove_stockcontroller.remove('banana')

# alterar_produto = StockController()
# alterar_produto.change('maçã', 'banana', 150, 'Fruits', 666)

# show_stock = StockController()
# show_stock.show()

test_register = SalesController()
test_register.register('banana', 'Edson Copque', 'Enéas Carneiro', 66)


# https://linktr.ee/edsoncopque