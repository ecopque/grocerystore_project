# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?

class CustomerController:
    def register(self, name, telephone, cpf, category):
        persondao_save = PersonDao.save()

        cpf_list = []
        for i1 in persondao_save:
            if i1.cpf == cpf:
                cpf_list.append(i1)