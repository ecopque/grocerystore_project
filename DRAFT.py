# File: /draft.py

from models import *
from dao import *

# Como posso remover um fornecedor da lista de fornecedores, se ele existir, e garantir que a lista seja atualizada e gravada em um arquivo de texto?


# Put uncategorized in stock:
salesdao_read = StockDao.read()

# Criando a lista de estoque de forma explícita com um loop for
# Put uncategorized in stock:
salesdao_read = StockDao.read()

# Alterando diretamente os itens de salesdao_read
for i in range(len(salesdao_read)):
    x = salesdao_read[i]
    if x.product.category == removecategory:
        # Substituindo diretamente o item na lista
        salesdao_read[i] = StockModel(ProductModel(x.product.name, x.product.price, 'uncategorized'), x.quantity)

# Escrevendo no arquivo
with open('hd_stock.txt', 'w') as file:
    for i4 in salesdao_read:
        file.writelines(i4.product.name + '|' +
                        i4.product.price + '|' +
                        i4.product.category + '|' +
                        str(i4.quantity))
        file.writelines('\n')

