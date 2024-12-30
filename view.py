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
                                'Enter 7 to access [see] top selling products\n'
                                'Enter 8 to exit: \n'))
                                    
        if ask_global == 1:
            categorycontroller = controller.CategoryController()
            while True:
                ask_categories = int(input('Enter 1 to [register] a category\n'
                                            'Enter 2 to [remove] a category\n'
                                            'Enter 3 to [change] a category\n'
                                            'Enter 4 to [show] registered categories\n'
                                            'Enter 5 to [exit]: \n'))
                
                if ask_categories == 1:
                    register_category = input('Enter the category you want to register: \n')
                    categorycontroller.register(register_category)

                elif ask_categories == 2:
                    remove_categoryold = input('Enter the category you want to remove: \n')
                    categorycontroller.remove(remove_categoryold)

                elif ask_categories == 3:
                    change_categoryold = input('Enter the category you want to change: \n')
                    change_categorynew = input('Enter the new category: \n')
                    categorycontroller.change(change_categoryold, change_categorynew)

                elif ask_categories == 4:
                    categorycontroller.show()
                
                else:
                    break
        
        elif ask_global == 2:
            stockcontroller = controller.StockController
            while True:
                ask_stock = int(input('Enter 1 to [register] a new product\n'
                                      'Enter 2 to [remove] a product\n'
                                      'Enter 3 to [change] a product\n'
                                      'Enter 4 to [view] a product\n'
                                      'Enter 5 to [exit]: \n'))
                                                      
                if ask_stock == 1:
                    register_name = input('Enter a new product: \n')
                    register_price = input('Enter a price of the product: \n')
                    register_category = input('Enter a category of the product: \n')
                    register_quantity = input('Enter a quantity of the product: \n')
                    stockcontroller.register(register_name, 
                                             register_price, 
                                             register_category, 
                                             register_quantity)

                elif ask_stock == 2:
                    remove_name = input('Enter the product you want to remove: \n')
                    stockcontroller.remove(remove_name)

                elif ask_stock == 3:
                    change_nametold = input('Enter a product you want to change: \n')
                    change_namenew = input('Enter the new product name: \n')
                    change_pricenew = input('Enter the new product price: \n')
                    change_categorynew = input('Enter the product category: \n')
                    change_quantitynew = input('Enter the product quantity')
                    stockcontroller.change(change_nametold, 
                                           change_namenew,
                                           change_pricenew,
                                           change_categorynew,
                                           change_quantitynew)
                
                elif ask_stock == 4:
                    stockcontroller.show()
                
                else:
                    break