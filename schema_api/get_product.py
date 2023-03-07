from schema import Schema


class GetProduct(Schema):
    name = str
    description = str
    price = int
    quantity = int



if __name__ == '__main__':
    g = GetProduct(name=1)
    print(g.get_dict())