# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?

class CustomerController:
    def change(self, nameOld, nameNew, telephoneNew, cpfNew, emailNew, addressNew):
        persondao_read = PersonDao.read()

        customer_name = []
        for i1 in persondao_read:
            if i1.name == nameOld:
                customer_name.append(i1)

        if len(customer_name) > 0:
            for i2 in range(len(persondao_read)):
                if persondao_read[i2].name == nameOld:
                    persondao_read[i2] = PersonModel(nameNew, telephoneNew, cpfNew, emailNew, addressNew)
            print(f'The customer {nameOld} updates successfully.')
        else:
            print('The customer you want to change does not exists.')
    
        with open('hd_customer.txt', 'w') as file:
            for i3 in persondao_read:
                file.writelines(i3.name + '|' +
                                i3.telephone + '|' +
                                ...)