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
                               'Enter 7 to access [Show] top selling products\n'
                               'Enter 8 to [exit]: \n'))
                                    
        if ask_global == 1:
            categorycontroller = controller.CategoryController()
            
            while True:
                ask_categories = int(input('Enter 1 to [register] a category\n'
                                           'Enter 2 to [remove] a category\n'
                                           'Enter 3 to [change] a category\n'
                                           'Enter 4 to [show] registered categories\n'
                                           'Enter 5 to [exit]: \n'))
                
                if ask_categories == 1:
                    category = input('Enter the category you want to register: \n')
                    categorycontroller.register(category)

                elif ask_categories == 2:
                    category = input('Enter the category you want to remove: \n')
                    categorycontroller.remove(category)

                elif ask_categories == 3:
                    categoryold = input('Enter the category you want to change: \n')
                    categorynew = input('Enter the new category: \n')
                    categorycontroller.change(categoryold, 
                                              categorynew)

                elif ask_categories == 4:
                    categorycontroller.show()
                
                else:
                    break
        
        elif ask_global == 2:
            stockcontroller = controller.StockController()
            
            while True:
                ask_stock = int(input('Enter 1 to [register] a new product\n'
                                      'Enter 2 to [remove] a product\n'
                                      'Enter 3 to [change] a product\n'
                                      'Enter 4 to [view] a product\n'
                                      'Enter 5 to [exit]: \n'))
                                                      
                if ask_stock == 1:
                    name = input('Enter a new product: \n')
                    price = input('Enter a price of the product: \n')
                    category = input('Enter a category of the product: \n')
                    quantity = input('Enter a quantity of the product: \n')
                    stockcontroller.register(name, 
                                             price, 
                                             category, 
                                             quantity)

                elif ask_stock == 2:
                    product = input('Enter the product you want to remove: \n')
                    stockcontroller.remove(product)

                elif ask_stock == 3:
                    nameold = input('Enter a product you want to change: \n')
                    namenew = input('Enter the new product name: \n')
                    pricenew = input('Enter the new product price: \n')
                    categorynew = input('Enter the product category: \n')
                    quantitynew = input('Enter the product quantity')
                    stockcontroller.change(nameold, 
                                           namenew,
                                           pricenew,
                                           categorynew,
                                           quantitynew)
                
                elif ask_stock == 4:
                    stockcontroller.show()
                
                else:
                    break

        elif ask_global == 3:
            suppliercontroller = controller.SupplierController()

            while True:
                ask_supplier = int(input('Enter 1 to [register] a supplier: \n'
                                         'Enter 2 to [remove] a supplier: \n'
                                         'Enter 3 to [change] a supplier: \n'
                                         'Enter 4 to [show] suppliers: \n'
                                         'Enter 5 to [exit]: '))
                
                if ask_supplier == 1:
                    name = input('Enter the supplier you want to register: \n')
                    cnpj = input('Enter the CNPJ you want to register: \n')
                    telephone = input('Enter the Telephone number you want to register: \n')
                    category = input('Enter the category you want to register: \n')
                    suppliercontroller.register(name, 
                                                cnpj, 
                                                telephone, 
                                                category)
                    
                elif ask_supplier == 2:
                    supplier = input('Enter the supplier you want to remove: \n')
                    suppliercontroller.remove(supplier)

                elif ask_supplier == 3:
                    nameold = input('Enter the supplier you want to change: \n')
                    namenew = input('Enter the new supplier you want to register: \n')
                    cnpjnew = input('Enter the new CNPJ you want to register: \n')
                    telephonenew = input('Enter the new Telephone you want to register: \n')
                    categorynew = input('Enter the new category you want to register: \n')
                    suppliercontroller.change(nameold,
                                              namenew,
                                              cnpjnew,
                                              telephonenew,
                                              categorynew)

                elif ask_supplier == 4:
                    suppliercontroller.show()

                else:
                    break

        elif ask_global == 4:
            customercontroller = controller.CustomerController()

            while True:
                ask_customer = int(input('Enter 1 to [register] a customer: \n'
                                         'Enter 2 to [remove] a customer: \n'
                                         'Enter 3 to [change] a customer: \n'
                                         'Enter 4 to [show] customers: \n'
                                         'Enter 5 to [exit]: \n'))
                
                if ask_customer == 1:
                    name = input('Enter the customer you want to register: \n')
                    telephone = input('Enter the telephone you want to register: \n')
                    cpf = input('Enter the CPF you want to register: \n')
                    email = input('Enter the email you want to register: \n')
                    address = input('Enter the address you want to register: \n')
                    customercontroller.register(name,
                                                telephone,
                                                cpf,
                                                email,
                                                address)

                elif ask_customer == 2:
                    name = input('Enter the customer you want to remove: \n')
                    customercontroller.remove(name)

                elif ask_customer == 3:
                    nameold = input('Enter the customer you want to change: \n')
                    namenew = input('Enter the new customer you want to change: \n')
                    telephonenew = input('Enter the telephone you want to change: \n')
                    cpfnew = input('Enter the new cpf you want to change: \n')
                    emailnew = input('Enter the new e-mail you want to change: \n')
                    addressnew = input('Enter the new address you want to change: \n')
                    customercontroller.change(nameold,
                                              namenew,
                                              telephonenew,
                                              cpfnew,
                                              emailnew,
                                              addressnew)
                
                elif ask_customer == 4:
                    customercontroller.show()
                
                else:
                    break

        elif ask_global == 5:
            employeecontroller = controller.EmployeeController()

            while True:
                ask_employee = int(input('Enter 1 to [register] a employee: \n'
                                         'Enter 2 to [remove] a employee: \n'
                                         'Enter 3 to [change] a employee: \n'
                                         'Enter 4 to [show] employees: \n'
                                         'Enter 5 to [exit]: \n'))
                
                if ask_employee == 1:
                    clt = input('Enter the employee CLT: \n')
                    name = input('Enter a employee name to register: \n')
                    telephone = input('Enter a Telephone Number to register: \n')
                    cpf = input('Enter a CPF number to register: \n')
                    email = input('Enter a e-mail to register: \n')
                    address = input('Enter the address to register: \n')
                    employeecontroller.register(clt,
                                                name,
                                                telephone,
                                                cpf,
                                                email,
                                                address)
                    
                elif ask_employee == 2:
                    name = input('Enter the employee you want to remove: \n')
                    employeecontroller.remove(name)

                elif ask_employee == 3:
                    nameold = input('Enter the employee you want to change: \n')
                    cltnew = input('Enter the CLT you want to register: \n')
                    namenew = input('Enter the new name you want to register: \n')
                    telephonenew = input('Enter the telephone you want to register: \n')
                    cpfnew = input('Enter the CPF you want to register: \n')
                    emailnew = input('Enter the e-mail you want to register: \n')
                    addressnew = input('Enter the address you wanto to register: \n')
                    employeecontroller.change(nameold,
                                              cltnew,
                                              namenew,
                                              telephonenew,
                                              cpfnew,
                                              emailnew,
                                              addressnew)

                elif ask_employee == 4:
                    employeecontroller.show()

                else:
                    break