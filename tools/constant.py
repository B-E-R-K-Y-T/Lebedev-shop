class Constant:
    def __setattr__(self, key, _):
        if key == key.upper():
            raise AttributeError(f'Attribute "{key}" is constant!')
