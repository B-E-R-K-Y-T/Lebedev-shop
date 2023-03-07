class Constant:
    def __setattr__(self, key, value):
        if key == key.upper():
            raise AttributeError(f'Attribute "{key}" is constant!')
        