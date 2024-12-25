# File: /draft.py

from models import *
from dao import *


class MethodName:
    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        method_name = self.method.__name__  # Obtém o nome do método sem importar nada
        class_name = self.__class__.__name__
        print(f'Calling method {method_name}() from class {class_name}')
        return self.method(*args, **kwargs)

class SupplierController:
    def __init__(self):
        self.change = MethodName(self.change)  # Aplica o método ao nosso manipulador de nome de método
        self.register = MethodName(self.register)  # Aplica o método ao nosso manipulador de nome de método

    def change(self, nameOld, nameNew, cnpjNew, telephoneNew, categoryNew):
        print(f'Changing supplier from {nameOld} to {nameNew}.')

    def register(self, name, cnpj, telephone, category):
        print(f'Registering new supplier: {name}.')

# Testando
controller = SupplierController()
controller.change("Old Supplier", "New Supplier", "123456789", "987654321", "Category")
controller.register("New Supplier", "987654321", "123456789", "Category")
