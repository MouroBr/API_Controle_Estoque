import json
from json import JSONEncoder

class Product:

    def __init__(self, id, type, brand, dateEntry, expirationDate):
        self.id = str(id)
        self.type = type
        self.brand = brand
        self.dateEntry = str(dateEntry)
        self.expirationDate = expirationDate
        
    def dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "brand": self.brand,
            "dateEntry": self.dateEntry,
            "expirationDate": self.expirationDate
        }
    
    def toJSON(self):
        return json.dumps(self, cls=ProductEncoder, indent=4)
       
class ProductEncoder(JSONEncoder):

    def default(self, o):
        return o.dict()

