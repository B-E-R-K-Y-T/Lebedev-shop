from tools.database import Base, database


class Cart(Base):
    __tablename__ = 'orders'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, nullable=False)
    total_price = database.Column(database.Integer, nullable=False)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return None