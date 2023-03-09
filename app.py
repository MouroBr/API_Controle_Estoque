from flask import Flask, make_response, jsonify, request
from product import productRepository

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/inventory', methods=['GET'])
def getAllProduct():
    allProduct = productRepository.getAllProducts()

    responseProduct = []
    for product in allProduct:
        responseProduct.append(product.to_json())

    return make_response(jsonify(responseProduct))


@app.route('/product/<product_id>', methods=['GET'])
def getProductById(product_id):
    product = productRepository.getById(product_id)
    return make_response(jsonify(product.to_json()))


@app.route('/addProduct', methods=['POST'])
def creatProduct():
    product = productRepository.create(request.json['tipe'],
                                       request.json['brand'],
                                       request.json['dateEntry'],
                                       request.json['expirationDate'])

    return make_response(jsonify(id=product.id), 201)


@app.route('/product/<product_id>', methods=['DELETE'])
def deleteproduct(product_id):
    if productRepository.removeById(product_id):
        return make_response([], 204)

    return make_response(jsonify([]), 404)


app.run()
