# File: /draft.py

#1: Criar método remove.
#2: Verificar se meu parâmetro é igual à categoria e armazenar.
#3: Verificar se escreveram algum caractere da categoria.
#4: Verificar se a categoria escrita é igual à categoria do hd.

def remove(self, removecategory):
    read_categorydao = CategoryDao.read()

    cat = []
    for i in read_categorydao:
        if i.category == removecategory:
            cat.append(i)

    if len(cat) <= 0:
        print('The category you want to remove does not exist.')
    else:
        for i in range(len(read_categorydao)):
            if read_categorydao[i] == removecategory:
                del read_categorydao[i]
                break
            print('Category removed successfully.')

            with open('hd_category.txt', 'w') as file:
                for i in read_categorydao:
                    file.writelines(i.category)
