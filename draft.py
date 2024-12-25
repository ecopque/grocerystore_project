# File: /draft.py

from models import *
from dao import *


def change(self, nameOld, nameNew, cnpjNew, telephoneNew, categoryNew):
    supplierdao_read = SupplierDao.read()

    data_list = []
    for x in supplierdao_read:
        if x.name == nameOld:
            data_list.append(x)

    if len(data_list) > 0:
        
        cnpj_list = []
        for x in supplierdao_read:
            if x.cnpj == cnpjNew:
                cnpj_list.append(x)

        if len(cnpj_list) == 0:
            supplier_update = []
            for x in supplierdao_read:
                if x.name == nameOld:
                    supplier_update.append(SupplierModel(nameNew, cnpjNew, telephoneNew, categoryNew))
                else:
                    supplier_update.append(x)
        else:
            print('The CNPJ already exists.')
            supplier_update = supplierdao_read
    else:
        print('The supplier you want to change does not exist.')
        supplier_update = supplierdao_read

    with open('hd_supplier.txt', 'w') as file:
        for i in supplier_update:
            file.writelines(i.name + '|' +
                            i.cnpj + '|' +
                            i.telephone + '|' +
                            str(i.category))
            file.writelines('\n')
        print('Supplier changed successfully.')
