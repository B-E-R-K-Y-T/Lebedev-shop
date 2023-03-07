class Schema:
    def __get_fields_sub_class(self):
        fields = dict()

        for field in dir(self):
            obj_subclass = self.__getattribute__(field)

            if not field.startswith('__') and isinstance(obj_subclass, type):
                fields[field] = obj_subclass

        return fields

    def __init__(self, **kwargs):
        self.fields_sub_class = self.__get_fields_sub_class()

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def get_dict(self):
        fields = self.fields_sub_class
        res = dict()

        for key, value in fields.items():
            attr = self.__getattribute__(key)
            if isinstance(attr, type):
                raise AttributeError(f'Attribute "{key}" in the class "{self.__class__.__name__}" is not defined!')
            else:
                res[key] = attr

        return res
