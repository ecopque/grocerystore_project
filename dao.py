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
        print(cls.category)

CategoryDao.save('Fruits')
CategoryDao.save('Vegetables')
CategoryDao.save('Legumes')

CategoryDao.read()