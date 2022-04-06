import matrix_exception


class Matrix:
    def __init__(self, data):
        self.__matrix = data

    #        self.rows = len(data)
    #        self.columns = len(data[0])
    #        for row in data:
    #            if len(row) != self.columns:
    #                raise matrix_exception.BadMatrixException
    #            for val in row:
    #                if type(val) is not int:
    #                    raise matrix_exception.BadMatrixException

    def __add__(self, other):
        try:
            if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
                sum_matrix = '\n'.join(' '.join(str(elem1 + elem2) for elem1, elem2 in zip(row1, row2))
                                       for row1, row2 in zip(self.__matrix, other.__matrix))
            else:
                raise matrix_exception.BadMatrixException
        except TypeError:
            # todo dif type of separators when rows and when columns: " " and "/n"
            sum_matrix = '\n'.join(str(elem1 + elem2) for elem1, elem2 in zip(self.__matrix, other.__matrix))
        return sum_matrix

    def __mul__(self, other):
        pass

    def __bool__(self):
        for row in self.__matrix:
            for elem in row:
                if elem != 0:
                    return True
        return False

    def __str__(self):
        try:
            result = '\n'.join(' '.join(str(elem) for elem in row) for row in self.__matrix)
            return f"{result}\n"
        except TypeError:
            # todo dif type of separators when rows and when columns: " " and "/n"
            result = ' '.join(str(elem) for elem in self.__matrix)
            return f"{result}\n"


def get_object(data):
    return Matrix(data)


if __name__ == '__main__':
    matrix1 = get_object(tuple((1, 2)))
    matrix2 = get_object(tuple((1, 2)))
    print(matrix1 + matrix2)
    print("hello")