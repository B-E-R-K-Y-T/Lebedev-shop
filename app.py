import sqlalchemy as db

from flask import Flask, jsonify, request
from tools.database import create_db, session
from settings.config import PATH_GET_PRODUCT_REQUEST, RequestMethod, PATH_CREATE_PRODUCT_REQUEST, \
    PATH_UPDATE_PRODUCT_REQUEST, PATH_DELETE_PRODUCT_REQUEST, PATH_CREATE_CART_REQUEST
from models.product import Product
from tools.request_worker import ProductRequest

app = Flask(__name__)
client = app.test_client()


@app.route(PATH_GET_PRODUCT_REQUEST, methods=[RequestMethod.GET])
def get_product(id_product):
    pr = ProductRequest()
    product = Product.query.filter(Product.id == id_product).first()
    serialized: dict = {}

    for key in pr.get_product_answer:
        serialized[key] = product[key]

    return jsonify(serialized)


@app.route(PATH_CREATE_PRODUCT_REQUEST, methods=[RequestMethod.POST])
def create_product():
    new_obj = Product(**request.json)
    session.add(new_obj)
    session.commit()
    serialized = {'id': new_obj.id}
    return jsonify(serialized)


@app.route(PATH_UPDATE_PRODUCT_REQUEST, methods=[RequestMethod.PUT])
def update_product(id_product):
    product = Product.query.filter(Product.id == id_product).first()
    params = request.json
    if product:
        for k, v in params.items():
            setattr(product, k, v)

        session.commit()

        return {'message': 'Все обновилось'}, 200
    else:
        return {'message': 'Не обновилось нихуя'}, 500


@app.route(PATH_DELETE_PRODUCT_REQUEST, methods=[RequestMethod.DELETE])
def delete_product(id_product):
    product = Product.query.filter(Product.id == id_product).first()
    if product:
        session.delete(product)
        session.commit()

        return {'message': 'Все удалилось'}, 200
    else:
        return {'message': 'Не удалилось нихуя'}, 500


# @app.route(PATH_CREATE_CART_REQUEST, methods=[RequestMethod.DELETE])
# def create_cart(id_product):
#     product = Product.query.filter(Product.id == id_product).first()
#     if product:
#         session.delete(product)
#         session.commit()
#
#         return {'message': 'Все удалилось'}, 200
#     else:
#         return {'message': 'Не удалилось нихуя'}, 500


if __name__ == '__main__':
    create_db()
    app.run()
