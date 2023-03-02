from tools.database import Base, database


class CartProducts(Base):
    __tablename__ = 'cart_products'

    count = database.Column(database.Integer, nullable=False)
    cart_id = database.Column(database.Integer, primary_key=True)
    product_id = database.Column(database.Integer, database.ForeignKey('cart.id'))

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return None
