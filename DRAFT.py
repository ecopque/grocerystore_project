# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?

class EmployeeController:
    def register(self, clt, name, telephone, cpf, email, address):
        employeedao_read = EmployeeDao.read()

        employee_cpf = []
        for i1 in employeedao_read:
            if i1.cpf == cpf:
                employee_cpf.append(i1)
        
        employee_clt = []
        for i2 in employeedao_read:
            if i2.clt == clt:
                employee_clt.append(i2)

        if len(employee_cpf) > 0:
            print('Employee already exists.')
        
        elif len(employee_clt) > 0:
            print('There is already an employee with this CLT.')
        
        else:
            if len(cpf) == 11 and len(telephone) >= 10 and len(telephone) <= 11:
                EmployeeDao.save(EmployeeModel(clt, name, telephone, cpf, email, address))
                print('Employee registered successfully.')
            else:
                print('Enter a valid CPF or Telephone number.')
        