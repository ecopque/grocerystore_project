# File: /view.py

import os.path
import controller

def createfiles(*args):
    for i1 in args:
        if not os.path.exists(i1):
            with open(i1, 'w') as file:
                file.write('')

createfiles('hd_category.txt',
            'hd_customer.txt',
            'hd_employee.txt',
            'hd_person.txt',
            'hd_sale.txt',
            'hd_stock.txt',
            'hd_supplier.txt')

if __name__ == '__main__':
    while True:
        ask_global = int(input('Enter 1 to access [Categories]\n'
                                'Enter 2 to access [Stock]\n'
                                'Enter 3 to access [Supplier]\n'
                                'Enter 4 to access [Customer]\n'
                                'Enter 5 to access [Employee]\n'
                                'Enter 6 to access [Sales]\n'
                                'Enter 7 to access see top selling products\n'
                                'Enter 8 to exit: \n'))
                                    
        if ask_global == 1:
            categorycontroller = controller.CategoryController()
            while True:
                ask_categories = int(input('Enter 1 to register a category\n'
                                            'Enter 2 to remove a category\n'
                                            'Enter 3 to change a category\n'
                                            'Enter 4 to show registered categories\n'
                                            'Enter 5 to exit: \n'))
                
                if ask_categories == 1:
                    category = input('Enter the category you want to register: \n')
                    categorycontroller.register(category)

                elif ask_categories == 2:
                    category = input('Enter the category you want to remove: \n')
                    categorycontroller.remove(category)

                elif ask_categories == 3:
                    category = input('Enter the category you want to change: \n')
                    categorynew = input('Enter the new category: \n')
                    categorycontroller.change(category, categorynew)

                elif ask_categories == 4:
                    categorycontroller.show()
                
                else:
                    break
        
        elif ask_global == 2:
            stockcontroller = controller.StockController
            while True:
                ask_stock = int(input('Enter 1 to register a new product\n'
                                      'Enter 2 to remove a product\n'
                                      'Enter 3 to change a product\n'
                                      'Enter 4 to view a product\n'
                                      'Enter 5 to exit: \n'))
                                                      
                if ask_stock == 1:
                    product = input('Enter a new product: \n')
                    price = input('Enter a price: \n')
                    stockcontroller.register(product, )
