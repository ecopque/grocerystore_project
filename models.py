# File: /models.py

from datetime import datetime

class CategoryModel:
    def __init__(self, category):
        self.category = category

class ProductModel:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class StockModel:
    def __init__(self, product: ProductModel, quantity):
        self.product = product
        self.quantity = quantity

class SalesModel:
    def __init__(self, items_sold: ProductModel, seller, buyer, quantity_sold, date = datetime.now().strftime('%d/%m/%Y')):
        self.items_sold = items_sold
        self.product = ProductModel
        self.seller = seller
        self.buyer = buyer
        self.quantity_sold = quantity_sold
        # self.sale = sale
        self.date = date

class SupplierModel:
    def __init__(self, name, cnpj, telephone, category):
        self.name = name
        self.cnpj = cnpj
        self.telephone = telephone
        self.category = category

class PersonModel:
    def __init__(self, name, telephone, cpf, email, address):
        self.name = name
        self.telephone = telephone
        self.cpf = cpf
        self.email = email
        self.address = address

class EmployeeModel(PersonModel):
    def __init__(self, clt, name, telephone, cpf, email, address):
        self.clt = clt
        super(EmployeeModel, self).__init__(name, telephone, cpf, email, address)

class CustomerModel(PersonModel):
    def __init__(self, name, telephone, cpf, email, address):
        super(EmployeeModel, self).__init__(name, telephone, cpf, email, address)


# Edson Copque | https://linktr.ee/edsoncopque