class Iterator:
    """ Iterates through source list/tuple/generator and returns values that match predicate condition """
    def __init__(self, source, predicate):
        self.__source = tuple(source)
        self.__predicate = predicate

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        while self.__index < len(self.__source):
            if self.__predicate(self.__source[self.__index]):
                result = self.__source[self.__index]
                self.__index += 1
                return result
            self.__index += 1
        raise StopIteration


def user_iterator(source, p):
    """ Same as class above, but implemented as a function """
    source = tuple(source)
    index = 0
    while index < len(source):
        if p(source[index]):
            yield source[index]
        index += 1


def get_object(source, predicate):
    return Iterator(source, predicate)
