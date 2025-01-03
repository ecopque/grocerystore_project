# FILE: /controller.py

from models import *
from dao import *
from datetime import datetime

class CategoryController:
    def register(self, categoryNew):
        categorydao_read = CategoryDao.read()
        
        exists_flag = False
        for i1 in categorydao_read:
            if i1.category == categoryNew: #11:
                exists_flag = True
        
        if not exists_flag:
            CategoryDao.save(categoryNew)
            print('Category registered successfully.')
        else:
            print('The category you want to register already exists.')

    def remove(self, categoryOld):
        categorydao_read = CategoryDao.read()

        # hd_compare_cat = list(filter(lambda x: x.category == categoryOld, categorydao_read))
        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == categoryOld:
                hd_compare_cat.append(i1)
    
        if len(hd_compare_cat) == 0:
            print('The category you want to remove does not exist.')
        
        else:
            for i2 in range(len(categorydao_read) -1, -1, -1): #12:
                if categorydao_read[i2].category == categoryOld:
                    del categorydao_read[i2]
            print('Category removed successfully.')
            
            with open('hd_category.txt', 'w') as file:
                    for i3 in categorydao_read:
                        file.writelines(i3.category)
                        file.writelines('\n')

        # Put 'uncategorized' on the stock product if removing the category
        stockdao_read = StockDao.read()

        # stock = list(map(lambda x: StockModel(ProductModel(x.product.name, x.product.price, 'uncategorized'), x.quantity) if x.product.category == removecategory else x, salesdao_read))
        for i4 in range(len(stockdao_read)):
            if stockdao_read[i4].product.category == categoryOld:
                stockdao_read[i4] = StockModel(ProductModel(
                    stockdao_read[i4].product.name, 
                    stockdao_read[i4].product.price, 
                    'uncategorized'), 
                    stockdao_read[i4].quantity)

        with open('hd_stock.txt', 'w') as file:
            for i4 in stockdao_read:
                file.writelines(i4.product.name + '|' +
                                i4.product.price + '|' +
                                i4.product.category + '|' +
                                str(i4.quantity))
                file.writelines('\n')

    def change(self, categoryOld, categoryNew):
        categorydao_read = CategoryDao.read()

        # hd_compare_cat = list(filter(lambda read_category: read_category.category == categoryOld, read_category))
        hd_compare_cat = []
        for i1 in categorydao_read:
            if i1.category == categoryOld:
                hd_compare_cat.append(i1)
        
        if len(hd_compare_cat) > 0:

            # hd_compare_cat2 = list(filter(lambda read_category: read_category.category == categoryNew, read_category))
            hd_compare_cat2 = []
            for i2 in categorydao_read:
                if i2.category == categoryNew:
                    hd_compare_cat2.append(i2)
            
            if len(hd_compare_cat2) == 0:

                # read_category = list(map(lambda read_category: CategoryModel(newcategory) if (read_category.category == changecategory) else (read_category), read_category))
                for i3 in range(len(categorydao_read)):
                    if categorydao_read[i3].category == categoryOld:
                        categorydao_read[i3].category = categoryNew
                print(f"Category '{categoryOld}' changed to '{categoryNew}' successfully.")

                # Change stock category.
                stockdao_read = StockDao.read()

                for i5 in range(len(stockdao_read)):
                    if stockdao_read[i5].product.category == categoryOld:
                        stockdao_read[i5] = StockModel(ProductModel(
                            stockdao_read[i5].product.name,
                            stockdao_read[i5].product.price,
                            categoryNew),
                            stockdao_read[i5].quantity)
                
                with open('hd_stock.txt', 'w') as file:
                    for i6 in stockdao_read:
                        file.writelines(i6.product.name + '|' +
                                        i6.product.price + '|' +
                                        i6.product.category + '|' +
                                        str(i6.quantity))
                        file.writelines('\n')
            else:
                print(f"The category '{categoryNew}' already exists.")
        else:
           print(f"The category '{categoryNew}' you want to change does not exist.")

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

            stock_temp.append(StockModel(ProductModel(i1.product.name, 
                                   i1.product.price, 
                                   i1.product.category), 
                                   i1.quantity))
        
        file = open('hd_stock.txt', 'w')
        file.write('')

        # [[Product('name', 'price', 'category'), quantity]]
        for i2 in stock_temp:
            with open('hd_stock.txt', 'a') as file:
                file.writelines(i2.product.name + '|' + 
                                i2.product.price + '|' + 
                                i2.product.category + '|' + 
                                str(i2.quantity))
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
        
    def report(self):
        salesdao_read = SalesDao.read()
        products = []

        for i1 in salesdao_read:
            name = i1.items_sold.name
            quantity = i1.quantity_sold

            # size = list(filter(lambda x: x['product'] == name, products))
            
            size = []
            for i2 in products: # filter
                if i2['product'] == name:
                    size.append(i2)
 
            if len(size) > 0:
                # products = list(map(lambda x: {'product': name, 'quantity': int(x['quantity']) + int(quantity)} if (x['product'] == name) else(x), products))

                for i3 in products:
                    if i3['product'] == name:
                        i3['quantity'] = int(i3['quantity']) + int(quantity)
            else:
                products.append({'product': name, 'quantity': int(quantity)}) #16:

        # ordered = sorted(products, key=lambda k: k['quantity'], reverse=True)
        ordered = products.copy()
        for i4 in range(len(ordered)):
            for j4 in range(i4 + 1, len(ordered)):
                if ordered[i4]['quantity'] < ordered[j4]['quantity']: #19:
                    ordered[i4], ordered[j4] = ordered[j4], ordered[i4] #19: # bubble sort

        print('These are the best selling products: ')
        number = 1
        for i5 in ordered:
            print(f'===== PRODUCT [{number}] =====')
            print(f'Product: {i5["product"]}\n'
                    f'Quantity: {i5["quantity"]}\n')
            number += 1

    def show(self, startDate, endDate):
        salesdao_read = SalesDao.read()
        startdate = datetime.strptime(startDate, '%d/%m/%Y')
        enddate = datetime.strptime(endDate, '%d/%m/%Y')

        # selected_sales = list(filter(lambda x: datetime.strptime(x.date, '%d/%m/%Y') >= startdate1 and datetime.strptime(x.date, '%d/%m/%Y') <= enddate1, salesdao_read))
        selected_sales = []
        for i1 in salesdao_read:
            sale_date = datetime.strptime(i1.date, '%d/%m/%Y')
            if sale_date >= startdate and sale_date <= enddate:
                selected_sales.append(i1)

        count_var = 1
        total_sales = 0

        for i2 in selected_sales:
            print(f'===== Sale [{count_var}] =====')
            print(f'Name: {i2.items_sold.name}\n'
                  f'Category: {i2.items_sold.category}\n'
                  f'Date: {i2.date}\n'
                  f'Quantity: {i2.quantity_sold}\n'
                  f'Buyer: {i2.buyer}\n'
                  f'Seller: {i2.seller}')
            
            total_sales += int(i2.items_sold.price) * int(i2.quantity_sold)
            count_var += 1

        print()
        print(f'Total sold: {total_sales}')

class SupplierController:
    def register(self, name, cnpj, telephone, category):
        supplierdao_read = SupplierDao.read()

        # cnpj_list = list(filter(lambda x: x.cnpj == cnpj, supplierdao_read))
        cnpj_list = []
        telephone_list = []

        for i1 in supplierdao_read:
            if i1.cnpj == cnpj:
                cnpj_list.append(i1)

        # telephone_list = list(filter(lambda x: x.telephone == telephone, supplierdao_read))
            if i1.telephone == telephone:
                telephone_list.append(i1)

        if len(cnpj_list) > 0:
            print('The CNPJ is already exists.')
        
        elif len(telephone_list) > 0:
            print('The telephone is already exists.')
        
        else:
            if len(cnpj) == 14 and len(telephone) <= 11 and len(telephone) >= 10:
                SupplierDao.save(SupplierModel(name, cnpj, telephone, category))
            else:
                print('Enter a valid CNPJ or Telephone number.')

    #A001:
    def change(self, nameOld, nameNew, cnpjNew, telephoneNew, categoryNew):
        supplierdao_read = SupplierDao.read()

        # supplier_name = list(filter(lambda x: x.name == nameOld, supplierdao_read)
        supplier_name = []
        for i1 in supplierdao_read:
            if i1.name == nameOld:
                supplier_name.append(i1)

        if len(supplier_name) > 0:
            # supplier_cnpj = list(filter(lambda x: x.cnpj == cnpjNew, supplierdao_read))
            supplier_cnpj = []
            for i2 in supplierdao_read:
                if i2.cnpj == cnpjNew:
                    supplier_cnpj.append(i2)

            # supplier_updated = list(map(lambda x: SupplierModel(nameNew, cnpjNew, telephoneNew, categoryNew) if(x.name == nameOld) else x, supplierdao_read))
            if len(supplier_cnpj) == 0:
                for i3 in range(len(supplierdao_read)):
                    if supplierdao_read[i3].name == nameOld:
                        supplierdao_read[i3] = SupplierModel(nameNew, cnpjNew, telephoneNew, categoryNew)
                        print(f'Supplier {nameOld} updated successfully.')
                        break
            else:
                print('The CNPJ already exists.')
        else:
            print('The supplier you want to change does not exists.')

        with open('hd_supplier.txt', 'w') as file:
            for i4 in supplierdao_read:
                file.writelines(i4.name + '|' +
                                i4.cnpj + '|' +
                                i4.telephone + '|' +
                                str(i4.category))
                file.writelines('\n')

    #A002:
    def remove(self, name):
        supplierdao_read = SupplierDao.read()

        # supplier_name = list(filter(lambda x: x.name == name, supplierdao_read))
        supplier_name = []
        for i1 in supplierdao_read:
            if i1.name == name:
                supplier_name.append(i1)
        
        if len(supplier_name) > 0:
            for i2 in range(len(supplierdao_read)):
                if supplierdao_read[i2].name == name:
                    print(f'Supplier {supplierdao_read[i2].name} ({supplierdao_read[i2].cnpj}) deleted.')
                    del supplierdao_read[i2]
                    break
        else:
            print('The supplier you want to remove does not exists.')
            return None
        
        with open('hd_supplier.txt', 'w') as file:
            for i3 in supplierdao_read:
                file.writelines(i3.name + '|' + 
                                i3.cnpj + '|' + 
                                i3.telephone + '|' +
                                str(i3.category))
                file.writelines('\n')
            print('Supplier removed successfully.')

    def show(self):
        supplierdao_read = SupplierDao.read()

        if len(supplierdao_read) == 0:
            print('The supplier list is empty.')

        for i1 in supplierdao_read:
            print('===== Suppliers =====')
            print(f'Category: {i1.category}\n'
                  f'Name: {i1.name}\n'
                  f'Telephone: {i1.telephone}\n'
                  f'CNPJ: {i1.cnpj}')

class CustomerController:
    def register(self, name, telephone, cpf, email, address):
        persondao_read = PersonDao.read()

        # cpf_list = list(filter(lambda x: x.cpf == cpf, persondao_read))
        cpf_list = []
        for i1 in persondao_read:
            if i1.cpf == cpf:
                cpf_list.append(i1)

        if len(cpf_list) > 0:
            print('CPF already exists.')

        else:
            if len(cpf) == 11 and len(telephone) >= 10 and len(telephone) <= 11:
                PersonDao.save(PersonModel(name, telephone, cpf, email, address))
                print('Customer registered successfully.')
            else:
                print('Enter a valid CPF os telephone number.')

    def change(self, nameOld, nameNew, telephoneNew, cpfNew, emailNew, addressNew):
        persondao_read = PersonDao.read()

        # customer_name = list(filter(lambda x: x.name == nameOld, persondao_read))
        customer_name = []
        for i1 in persondao_read:
            if i1.name == nameOld:
                customer_name.append(i1)
        
        if len(customer_name) > 0:
            # persondao_read = list(map(lambda x: PersonModel(nameNew, telephoneNew, cpfNew, emailNew, addressNew) if x.name == nameOld else x, persondao_read))
            for i2 in range(len(persondao_read)):
                if persondao_read[i2].name == nameOld:
                    persondao_read[i2] = PersonModel(nameNew, telephoneNew, cpfNew, emailNew, addressNew)
            print(f'Customer {nameOld} updates successfully.')
        else:
            print('The customer you want to change does not exists.')

        with open('hd_customers.txt', 'w') as file:
            for i3 in persondao_read:
                file.writelines(i3.name + '|' +
                                i3.telephone + '|' +
                                i3.cpf + '|' +
                                str(i3.email) + '|' +
                                str(i3.address))
                file.writelines('\n')
            print('Customer data saved successfully.')

    def remove(self, name):
        persondao_read = PersonDao.read()
        
        # customer_name = list(filter(lambda x: x.name == name, persondao_read)
        customer_name = []
        for i1 in persondao_read:
            if i1.name == name:
                customer_name.append(i1)
        
        if len(customer_name) > 0:
            for i2 in range(len(persondao_read)):
                if persondao_read[i2].name == name:
                    print(f'Customer {persondao_read[i2].name} deleted.')
                    del persondao_read[i2]
                    break
        else:
            print('The customer you want to delete does not exists.')
            return None
        
        with open('hd_customer.txt', 'w') as file:
            for i3 in persondao_read:
                file.writelines(i3.name + '|' +
                                i3.telephone + '|' +
                                i3.cpf + '|' +
                                i3.email + '|' +
                                str(i3.address))
                file.writelines('\n')
            print('Customers updated successfully.')

    def show(self):
        persondao_read = PersonDao.read()

        if len(persondao_read) == 0:
            print('Empty customer list.')

        for i1 in persondao_read:
            print('===== Customers =====')
            print(f'Name: {i1.name}\n'
                  f'Telephone: {i1.telephone}\n'
                  f'CPF: {i1.cpf}\n'
                  f'E-mail: {i1.email}\n'
                  f'Address: {i1.address}')

class EmployeeController:
    def register(self, clt, name, telephone, cpf, email, address):
        employeedao_read = EmployeeDao.read()

        # employee_cpf = list(filter(lambda x: x.cpf == cpf, employeedao_read))
        employee_cpf = []
        for i1 in employeedao_read:
            if i1.cpf == cpf:
                employee_cpf.append(i1)

        # employee_clt = list(filter(lambda x: x.clt == clt, employeedao_read))
        employee_clt = []
        for i2 in employeedao_read:
            if i2.clt == clt:
                employee_clt.append(i2)

        if len(employee_clt) > 0:
            print('CPF already exists.')
        
        elif len(employee_clt) > 0:
            print('There is already an employee with this CLT.')

        else:
            if len(cpf) == 11 and len(telephone) >= 10 and len(telephone) <= 11:
                EmployeeDao.save(EmployeeModel(clt, name, telephone, cpf, email, address))
                print('Employee registered successfully.')
            else:
                print('Enter a valid CPF or Telephone number.')

    def change(self, nameOld, cltNew, nameNew, telephoneNew, cpfNew, emailNew, addressNew):
        employeedao_read = EmployeeDao.read()

        # employee_name = list(filter(lambda x: x.name == nameOld, employeedao_read))
        employee_name = []
        for i1 in employeedao_read:
            if i1.name == nameOld:
                employee_name.append(i1)
        
        if len(employee_name) > 0:
            # employeedao_read = list(map(lambda x: EmployeeModel(cltNew, nameNew, telephoneNew, cpfNew, emailNew, addressNew) if x.name == nameOld else x, employeedao_read))
            for i2 in range(len(employeedao_read)):
                if employeedao_read[i2].name == nameOld:
                    employeedao_read[i2] = EmployeeModel(cltNew, nameNew, telephoneNew, cpfNew, emailNew, addressNew)
                    print(f'The employee {nameOld} updates successfully.')
                else:
                    print('The employee you want to change does not exists.')
        with open('hd_employee.txt', 'w') as file:
            for i3 in employeedao_read:
                file.writelines(i3.clt + '|' +
                                i3.name + '|' +
                                i3.telephone + '|' +
                                i3.cpf + '|' +
                                i3.email + '|' +
                                str(i3.address))
                file.writelines('\n')
            print('Employee altered successfully.')

    def remove(self, name):
        employeedao_read = EmployeeDao.read()

        # employee_name = list(filter(lambda x: x.name == name, employeedao_read))
        employee_name = []
        for i1 in employeedao_read:
            if i1.name == name:
                employee_name.append(i1)

        if len(employee_name) > 0:
            for i2 in range(len(employeedao_read)):
                if employeedao_read[i2].name == name:
                    del employeedao_read[i2]
                    break
        else:
            print('The employee you want to remove does not exists.')
            return None
        
        with open('hd_employee.txt', 'w') as file:
            for i3 in employeedao_read:
                file.writelines(i3.clt + '|' +
                                i3.name + '|' +
                                i3.telephone + '|' +
                                i3.cpf + '|' +
                                i3.email + '|' +
                                str(i3.address))
                file.writelines('\n')
            print('Employee removed successfully.')

    def show(self):
        employeedao_read = EmployeeDao.read()

        if len(employeedao_read) == 0:
            print('Empty employee list.')

        for i1 in employeedao_read:
            print('===== Employee =====')
            print(f'CLT: {i1.clt}\n'
                  f'Name: {i1.name}\n'
                  f'Telephone: {i1.telephone}\n'
                  f'CPF: {i1.cpf}\n'
                  f'E-mail: {i1.email}'
                  f'Address: {i1.address}')
            
        
                
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

# test_stockcontroller = StockController()
# test_stockcontroller.register('pera', 5, 'Fruits', 100)
# test_salescontroller = SalesController()
# test_salescontroller.register('maca', 'Edson Copque', 'Enéas Carneiro', 5)
# test_report_salescontroller = SalesController()
# test_report_salescontroller.report()

# test_salescontroller_show = SalesController()
# test_salescontroller_show.show('23/12/2024', '24/12/2024')

# test_suppliercontroller_register = SupplierController()
# test_suppliercontroller_register.register('Edson', '02666679690194', '1224888890', 'Work')

# test_suppliercontroller_change = SupplierController()
# test_suppliercontroller_change.change("Edsuuuu", "Edson", "111188831", "123338823", "Spartan")

# test_suppliercontroller_remove = SupplierController()
# test_suppliercontroller_remove.remove('Edsuuu')

# test_suppliercontroller_show = SupplierController()
# test_suppliercontroller_show.show()

# test_customercontroller_register = CustomerController()
# test_customercontroller_register.register('Steve Vai', '9458973564', '95665253215', 'me@vai.com', 'Hydra Institute')

# test_CustomerController_change = CustomerController()
# test_CustomerController_change.change('Carl Sagan', 'Yngwie Malmsteen', '12345678912345', '12345678912', 'me@yngwie.com', 'Rising Force')   

# test_customercontroller_remove = CustomerController()
# test_customercontroller_remove.remove('Carl Sagan')

# test_customercontroller_show = CustomerController()
# test_customercontroller_show.show()

# test_employeecontroller_register = EmployeeController()
# test_employeecontroller_register.register('123', 'Joe Satriani', '12345678912', '12345678912', 'me@satriani.org', 'Highway Star')

# test_employeecontroller_change = EmployeeController()
# test_employeecontroller_change.change('Joe Satriani', '666', 'Jimi Hendrix', '12345678912', '12345678912', 'me@jimihendrix.com', 'Experience')

# test_employeecontroller_remove = EmployeeController()
# test_employeecontroller_remove.remove('Steve Ray Vaughan')

# test_employeecontroller_show = EmployeeController()
# test_employeecontroller_show.show()

# test_categorycontroller_remove = CategoryController()
# test_categorycontroller_remove.remove('Vegetables')

# test_categorycontroller_change = CategoryController()
# test_categorycontroller_change.change('Fruits', 'Fruits2')

# Edson Copque | https://linktr.ee/edsoncopque