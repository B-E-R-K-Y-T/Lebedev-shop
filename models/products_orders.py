from tools.database import Base, database


class CartsProducts(Base):
    __tablename__ = 'products_orders'

    count = database.Column(database.Integer, nullable=False)
    order_id = database.Column(database.Integer, primary_key=True)
    product_id = database.Column(database.Integer, database.ForeignKey('carts.id'))

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return None
