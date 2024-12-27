# File: /draft.py

from models import *
from dao import *

class SuppplierController:
    def change(self, nameOld, nameNew, cnpjNew, telephoneNew, categoryNew):
        supplierdao_read = SupplierDao.read()

        supplier_names = []
        for i1 in supplierdao_read:
            if i1.name == nameOld:
                supplier_names.append(i1)

        if len(supplier_names) > 0:
       
            supplier_cnpj = []
            for i2 in supplierdao_read:
                if i2.cnpj == cnpjNew:
                    supplier_cnpj.append(i2)

            if supplier_cnpj == 0:
                supplier_changed = []
                for i3 in supplierdao_read:
                    if i3.name == nameOld:
                        supplier_changed.append(SupplierModel(nameNew, cnpjNew, telephoneNew, categoryNew))
                    else:
                        supplier_changed.append(i3)
            else:
                print('The CNPJ already exists.')
                supplier_changed = supplierdao_read
        else:
            print('The supplier you want to change does not exists.')
            supplier_changed = supplierdao_read

        with open('hd_supplier.txt', 'w') as file:
            for i4 in supplier_changed:
                file.writelines(i4.name + '|' +
                                i4.cnpj + '|' + )
                                