# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?

class SupplierController:
    def remove(self, name):

        supplierdao_read = SupplierDao.read()

        supplier_name = []
        for i1 in supplierdao_read:
            if i1.name == name:
                supplier_name.append(i1)

        if len(supplier_name) > 0:
            for i2 in range(len(supplierdao_read)):
                if supplierdao_read[i2].name == name:
                    print('xxx')
                    del supplierdao_read[i2]
                    break

            for i3 in supplierdao_read:
                if i3.name == name: ######
                    del supplierdao_read[i3]
                    break
        else:
            print('The supplier you want to remove does not exists.')