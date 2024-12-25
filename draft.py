# File: /draft.py

from models import *
from dao import *

class SupplierController:
    def register(self, name, cnpj, telephone, category):
        supplierdao_read = SupplierDao.read()

        cnpj_list = []
        telephone_list = []

        for i1 in supplierdao_read:
            if i1.cnpj == cnpj:
                cnpj_list.append(i1)

            if i1.telephone == telephone:
                telephone_list.append(i1)

        
        if len(cnpj_list) > 0:
            print('The CNPJ already exists.')
        
        elif len(telephone_list) > 0:
            print('The Telephone already exists.')
        
        else:
            if len(cnpj) == 14 and len(telephone) <= 11 and len(telephone) >= 10:
                SupplierDao.save(SupplierModel(name, cnpj, telephone, category))
            else:
                print('Enter a valid CNPJ or Telephone.')