from tools.constant import Constant

# ENGINE_DATABASE = "postgresql+psycopg2://root:root@labserv_db.serv.xamex.tech:5432/lab1db"
ENGINE_DATABASE = 'sqlite:///data/db.sqlite'


# Методы запросов
class RequestMethod(Constant):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


# Запросы:
# ======================================================================================================================
#
#                                       __________Товары____________
#
# ======================================================================================================================


# Create (Создание товара)
# Метод: POST /products
PATH_CREATE_PRODUCT_REQUEST = '/products'
CREATE_PRODUCT_REQUEST = {
    'name': '',
    'description': '',
    'price': 0,
    'quantity': 0,
}
# ANSWER:
CREATE_PRODUCT_ANSWER = {
  'id': 0,
}


# Read (Чтение товара)
# GET /products/{id}
PATH_GET_PRODUCT_REQUEST = '/products/<int:id_product>'
# Ответ:
GET_PRODUCT_ANSWER = {
    'id': 0,
    'name': '',
    'description': '',
    'quantity': 0,
    'price': 0,
}


# Update (Обновление товара)
# PUT /products/{id}
PATH_UPDATE_PRODUCT_REQUEST = '/products/<int:id_product>'
UPDATE_PRODUCT_REQUEST = {
    'price': 0,
}
# Ответ:
# выдать статус 200 если ок, иначе 500 !!!!!!!!!!!!!!!!!!!!1

# Delete (Удаление товара)
#
# DELETE /products/{id}
PATH_DELETE_PRODUCT_REQUEST = '/products/<int:id_product>'

# ======================================================================================================================
#
#                                       __________Корзины_____________
#
# ======================================================================================================================


# Create (Создание корзины)
# POST /carts
PATH_CREATE_CART_REQUEST = '/carts'
CREATE_CART_REQUEST = {
    'user_id': 0,
}
# Ответ:
CREATE_CART_ANSWER = {
    'id': 0,
}


# Read (Чтение корзины)
# GET /carts/{id}
PATH_GET_CART_REQUEST = '/carts/<int:id_cart>'
# Ответ:
GET_CART_ANSWER = {
  'id': 0,
  'user_id': 0,
  'total_price': 0,
  'items': [
    {
      'product_id': 0,
      'quantity': 0,
      'price': 0
    }
  ]
}


# Update (Обновление корзины)
# PUT /carts/{id}
PATH_UPDATE_CART_REQUEST = '/carts/<int:id_cart>'
UPDATE_CART_REQUEST = {
  'id': 0,
  'items': [
    {
      'product_id': 0,
      'quantity': 0,
      'price': 0
    }
  ]
}
# Ответ:
UPDATE_CART_ANSWER = {
    'total_price': 0,
}


# DELETE /carts/{id}
#
# ОТвет: 200 или 400 ошибка бизнес логики, если нет товара (не обязательно к реализации) !!!!!!!!!!!!!


#
# Создание заказа
#
# put/orders
