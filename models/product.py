from tools.database import Base, database


class Product(Base):
    __tablename__ = 'products'

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(250), nullable=False)
    description = database.Column(database.String(500), nullable=False)
    price = database.Column(database.Integer, nullable=True)
    quantity = database.Column(database.Integer, nullable=True)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return None
