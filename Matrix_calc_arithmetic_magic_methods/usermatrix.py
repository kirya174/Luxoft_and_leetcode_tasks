import matrix_exception


class Matrix:
    def __init__(self, data):
        self.__matrix = data

    def __add__(self, other):
        try:
            if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):
                sum_matrix = tuple([tuple([(elem1 + elem2) for elem1, elem2 in zip(row1, row2)])
                                    for row1, row2 in zip(self.__matrix, other.__matrix)])
            else:
                raise matrix_exception.BadMatrixException
        except TypeError:
            if len(self.__matrix) > 1:
                sum_matrix = [(elem1 + elem2, ) for elem1, elem2 in zip(self.__matrix, other.__matrix)]
            else:
                sum_matrix = [(elem1 + elem2) for elem1, elem2 in zip(self.__matrix[0], other.__matrix[0])]
        return Matrix(sum_matrix)

    def __mul__(self, other):
        rows_a = len(self.__matrix)
        cols_a = len(self.__matrix[0])
        cols_b = len(other.__matrix[0])
        output = [[0 for row in range(cols_b)] for col in range(rows_a)]

        if rows_a == cols_b:
            for i in range(rows_a):
                for j in range(cols_b):
                    for k in range(cols_a):
                        output[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
            return Matrix(output)
        else:
            raise matrix_exception.BadMatrixException

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
            if len(self.__matrix) > 1:
                result = '\n'.join(str(elem) for elem in self.__matrix)
            else:
                result = ' '.join(str(elem) for elem in self.__matrix)
            return f"{result}\n"


def get_object(data):
    return Matrix(data)


if __name__ == '__main__':
    matrix1 = get_object(((0, 0, 1), (0, 0, 1), (0, 0, 2)))
    matrix2 = get_object(((1, 2, 1), (2, 2, 1), (2, 2, 2)))
    print(matrix1 * matrix2)
