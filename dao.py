# File: /dao.py
# Data Access Object

from models import *

class CategoryDao:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open('category.txt', 'r') as file:
            cls.category = file.readlines()
        # cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))
        for i in range(len(cls.category)):
            cls.category[i] = cls.category[i].replace('\n', '')
        print(cls.category)

        cat = [] #1:
        for i in cls.category: #1:
            cat.append(CategoryModel(i)) #1:

CategoryDao.save('Fruits')
CategoryDao.save('Vegetables')
CategoryDao.save('Legumes')

CategoryDao.read()