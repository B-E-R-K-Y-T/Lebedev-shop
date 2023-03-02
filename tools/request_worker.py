from settings.config import *


class ProductRequest:
    def __init__(self):
        self.create_product_request = CREATE_PRODUCT_REQUEST
        self.create_product_answer = CREATE_PRODUCT_ANSWER
        self.get_product_answer = GET_PRODUCT_ANSWER
        self.update_product_request = UPDATE_PRODUCT_REQUEST


class CartRequest:
    def __init__(self):
        self.create_cart_request = CREATE_CART_REQUEST
        self.create_cart_answer = CREATE_CART_ANSWER
        self.get_cart_answer = GET_CART_ANSWER
        self.update_cart_request = UPDATE_CART_REQUEST
        self.update_cart_answer = UPDATE_CART_ANSWER
