# File: /draft.py

from models import *
from dao import *

class SupplierController:
    def change(self, nameOld, nameNew, cnpjNew, telephoneNew, categoryNew):
        supplierdao_read = SupplierDao.read()

        