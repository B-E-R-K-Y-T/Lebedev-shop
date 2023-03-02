from tools.database import Base, database


class Cart(Base):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    u_name = database.Column(database.Text, nullable=False)
    email = database.Column(database.Text, nullable=False)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            return None