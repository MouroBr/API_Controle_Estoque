import uuid
from product.products import Product

INVENTORY_MEMORY = []


def create(type, brand, dateEntry, expirationDate):
    product = Product(uuid.uuid4(), type, brand, dateEntry, expirationDate)
    INVENTORY_MEMORY.append(product)
    return product


def removeById(id):
    for product in INVENTORY_MEMORY:
        if product.id == id:
            INVENTORY_MEMORY.remove(product)
            return True

    return False


def getById(id):
    for product in INVENTORY_MEMORY:
        if product.id == id:
            return product


def getAllProducts():
    return INVENTORY_MEMORY