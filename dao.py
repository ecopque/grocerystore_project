# File: /dao.py
# Data Access Object

from models import *

class CategoryDao:
    @classmethod
    def save(cls, category):
        with open('hd_category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_category.txt', 'r') as file:
            cls.category = file.readlines()
        
        # cls.category = list(map(lambda x: x.replace('\n', ''), cls.category)) #2:
        for i in range(len(cls.category)):
            cls.category[i] = cls.category[i].replace('\n', '')
        print(cls.category)

        cat = [] #1:
        for i in cls.category: #1:
            cat.append(CategoryModel(i)) #1:
        return cat

class SalesDao:
    @classmethod
    def save(cls, sale: SalesModel):
        with open('hd_sale.txt', 'a') as file:
            file.writelines(sale.items_sold.name + '|' + 
                            str(sale.items_sold.price) + '|' + 
                            sale.items_sold.category + '|' + 
                            sale.seller + '|' + 
                            sale.buyer + '|' + 
                            str(sale.quantity_sold) + '|' + 
                            sale.date) #3:
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_sale.txt', 'r') as file:
            cls.sale = file.readlines()

        for i in range(len(cls.sale)):
            cls.sale[i] = cls.sale[i].replace('\n', '')
        print(cls.sale) #5:

        for i in range(len(cls.sale)):
            cls.sale[i] = cls.sale[i].split('|')
        print(cls.sale) #6:

        hd_sale = []
        for i in cls.sale:
            hd_sale.append(SalesModel(ProductModel(i[0], float(i[1]), i[2]), i[3], i[4], int(i[5]), i[6]))
        return hd_sale

class StockDao:
    @classmethod
    def save(cls, product: ProductModel, quantity):
        with open('hd_stock.txt', 'a') as file:
            file.writelines(product.name + '|' + 
                            str(product.price) + '|' + 
                            product.category + '|' + 
                            str(quantity))
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_stock.txt', 'r') as file:
            cls.stock = file.readlines()

        for i in range(len(cls.stock)):
            cls.stock[i] = cls.stock[i].replace('\n', '')
        print(cls.stock)

        for i in range(len(cls.stock)):
            cls.stock[i] = cls.stock[i].split('|')
        print(cls.stock)

        hd_stock = []
        for i in cls.stock:
            hd_stock.append(StockModel(ProductModel(i[0], i[1], i[2]), int(i[3])))
        return hd_stock

class SupplierDao:
    @classmethod
    def save(cls, supplier: SupplierModel):
        with open('hd_supplier.txt', 'a') as file:
            file.writelines(supplier.name + '|' + 
                            supplier.cnpj + '|' + 
                            supplier.telephone + '|' + 
                            supplier.category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_supplier.txt', 'r') as file:
            cls.supplier = file.readlines()

        for i in range(len(cls.supplier)):
            cls.supplier[i] = cls.supplier[i].replace('\n', '')
        print(cls.supplier)

        for i in range(len(cls.supplier)):
            cls.supplier[i] = cls.supplier[i].split('|')

        hd_supplier = []
        for i in cls.supplier:
            hd_supplier.append(SupplierModel(i[0], i[1], i[2], i[3]))
        return hd_supplier

class PersonDao:
    @classmethod
    def save(cls, person: PersonModel):
        with open('hd_person.txt', 'a') as file:
            file.writelines(person.name + '|' +
                            person.telephone + '|' +
                            person.cpf + '|' + 
                            person.email + '|' + 
                            person.address)
            file.writelines('\n')
    
    @classmethod
    def read(cls):
        with open('hd_person.txt', 'r') as file:
            cls.person = file.readlines()

        for i in range(len(cls.person)):
            cls.person[i] = cls.person[i].replace('\n', '')
        print(cls.person)

        for i in range(len(cls.person)):
            cls.person[i] = cls.person[i].split('|')
        print(cls.person)

        hd_person = []
        for i in cls.person:
            hd_person.append(PersonModel(i[0], i[1], i[2], i[3], i[4]))
        return hd_person
    
class EmployeeDao:
    @classmethod
    def save(cls, employee: EmployeeModel):
        with open('hd_employee.txt', 'a') as file:
            file.writelines(employee.clt + '|' +
                            employee.name + '|' +
                            employee.telephone + '|' +
                            employee.cpf + '|' +
                            employee.email + '|' +
                            employee.address)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('hd_employee.txt', 'r') as file:
            cls.employee = file.readlines()

        for i in range(len(cls.employee)):
            cls.employee[i] = cls.employee[i].replace('\n', '')
        print(cls.employee)

        for i in range(len(cls.employee)):
            cls.employee[i] = cls.employee[i].split('|')
        print(cls.employee)

        hd_employee = []
        for i in cls.employee:
            hd_employee.append(EmployeeModel(i[0], i[1], i[2], i[3], i[4], i[5]))
        return hd_employee

class CustomerDao:
    @classmethod
    def save(cls, customer: CustomerModel):
        with open('hd_customer.txt', 'a') as file:
            file.writelines(customer.name + '|' +
                            customer.telephone + '|' +
                            customer.cpf + '|' +
                            customer.email + '|' +
                            customer.address)
            file.writelines('\n')
    
    @classmethod
    def read(cls):
        with open('hd_customer.txt', 'r') as file:
            cls.customer = file.readlines()

            for i in range(len(cls.customer)):
                cls.customer[i] = cls.customer[i].replace('\n', '')
            print(cls.customer)

            for i in range(len(cls.customer)):
                cls.customer[i] = cls.customer[i].split('|')
            print(cls.customer)

            hd_customer = []
            for i in cls.customer:
                hd_customer.append(CustomerModel(i[0], i[1], i[2], i[3], i[4]))
            return hd_customer

# CategoryDao.save('Fruits')
# CategoryDao.save('Vegetables')
# CategoryDao.save('Legumes')
# CategoryDao.read() #4:

# p1_product = ProductModel('bean', 7, 'Legumes')
# p1_sale = SalesModel(p1_product, 'Edson', 'Théo', 3)
# SalesDao.save(p1_sale)
# SalesDao.read() # (#5, #6)

stockdao = StockDao()
stockdao.read()

# x = SalesDao.read()
# print(x[0].buyer) #7:
# print(x[0].items_sold.name) #8:
# print(x[0].items_sold.price) #9:


# Edson Copque | https://linktr.ee/edsoncopque