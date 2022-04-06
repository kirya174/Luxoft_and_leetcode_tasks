def get_object(data):
    return Deserializer(data)


class Deserializer:
    def __init__(self, data):
        # self.__dict = {}
        object.__setattr__(self, "_Deserializer__dict", {})
        for key, value in data:
            self.__dict[key] = value

    def __getattr__(self, attr):
        ''' Используется при обращении к известному аттрибуту класса через точку "Instance.attr" '''
        return self.__dict[attr]

    def __setattr__(self, attr, val):
        ''' Используется при записи в аттрибут класса через точку "Instance.attr = value" '''
        dict = self.__dict
        dict[attr] = val

    def __getitem__(self, item):
        ''' Используется при обращении к известному аттрибуту класса через квадратные скобки "Instance.["attr"]" '''
        return self.__dict[item]


if __name__ == '__main__':
    x = Deserializer((("f1", 1), ("f2", 2), ("f3", 3)))
    x.f4 = 5
    print(x.f4)