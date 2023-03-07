class Schema:
    def __get_fields_sub_class(self):
        fields = dict()

        for field in dir(self):
            obj_subclass = self.__getattribute__(field)

            if not field.startswith('__') and isinstance(obj_subclass, type):
                fields[field] = obj_subclass

        return fields

    def __check_type_attr(self, attr_name, attr_value):
        return type(attr_value.__name__) == self.fields_sub_class[attr_name]

    def __init__(self, **kwargs):
        self.fields_sub_class = self.__get_fields_sub_class()
        print(self.fields_sub_class)

        for key, value in kwargs.items():
            if key in self.fields_sub_class.keys():
                self.__setattr__(key, value)
            else:
                raise AttributeError(f'Attribute "{key}" in the class "{self.__class__.__name__}" is not exist!')

    def get_dict(self):
        fields = self.fields_sub_class
        res = dict()

        for key, value in fields.items():
            attr = self.__getattribute__(key)
            if self.__check_type_attr(attr_name=key, attr_value=value):
                raise AttributeError(f'Attribute "{key}" in the class "{self.__class__.__name__}" have invalid type!')
            elif isinstance(attr, type):
                raise AttributeError(f'Attribute "{key}" in the class "{self.__class__.__name__}" is not defined!')
            else:
                res[key] = attr

        return res
