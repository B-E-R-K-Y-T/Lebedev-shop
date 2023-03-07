from schema import Schema


class GetProduct(Schema):
    name = str
    description = str
    price = int
    quantity = int
    test = list[str]


if __name__ == '__main__':
    g = GetProduct(name='1', description='2', price=1, quantity=1, test=[])
    print(g.get_dict())
