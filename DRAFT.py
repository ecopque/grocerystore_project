# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?

def change(self, nameOld, nameNew, telephoneNew, cpfNew, emailNew, addressNew):
    # Lê todos os registros de pessoas
    persondao_read = PersonDao.read()

    # Inicializa uma lista para armazenar os clientes que correspondem ao nome antigo
    customer_name = []
    for i1 in persondao_read:
        if i1.name == nameOld:
            customer_name.append(i1)
    
    # Verifica se encontramos algum cliente com o nome antigo
    if len(customer_name) > 0:
        # Para cada pessoa, verifica se o nome é o 'nameOld' e realiza a atualização
        for i2 in range(len(persondao_read)):
            if persondao_read[i2].name == nameOld:
                persondao_read[i2] = PersonModel(nameNew, telephoneNew, cpfNew, emailNew, addressNew)
        
        # Imprime mensagem de sucesso após a atualização
        print(f'Customer {nameOld} updated successfully.')
    else:
        # Caso não encontre o cliente, imprime mensagem de erro
        print('The customer you want to change does not exist.')

    # Escreve os dados de volta no arquivo
    with open('hd_customers.txt', 'w') as file:
        for i2 in persondao_read:
            file.writelines(i2.name + '|' +
                            i2.telephone + '|' +
                            i2.cpf + '|' +
                            str(i2.email) + '|' +
                            str(i2.address))
            file.writelines('\n')

    # Imprime a mensagem de sucesso após salvar os dados
    print('Customer data saved successfully.')
