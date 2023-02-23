import json
from json import JSONEncoder

class Inventory:

    def __init__(self, unitis, id):
        self.unitis = unitis
        self.id = str(id)

    
    
    def toJSON(self):
        return json.loads(json.dumps(self, cls=ProductEncoder, indent=4))

       
class ProductEncoder(JSONEncoder):

    def default(self, o):
        return o.dict