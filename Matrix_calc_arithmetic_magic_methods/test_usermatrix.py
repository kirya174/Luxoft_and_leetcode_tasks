import pytest

import usermatrix
import matrix_exception


def create_matrix_object(rows, columns):
    data = usermatrix.get_object((tuple(i for i in range(columns)) for c in range(rows)))
    return data


def printed_matrix(data):
    return "\n".join(" ".join(str(elem) for elem in row) for row in data)


def test_matrix_created():
    matrix = create_matrix_object(3, 3)
    assert type(matrix) is usermatrix.Matrix


@pytest.mark.parametrize("data, expected", [
    (((1, 2), (1, 2), (1, 2)), True),
    (((0, 0), (0, 0), (0, 0)), False),
])
def test_bool_returns_correct_value(data, expected):
    assert bool(usermatrix.get_object(tuple(data))) == expected


@pytest.fixture()
@pytest.mark.parametrize("data, result", [
    (((1, 2), (1, 2), (1, 2)), f'1 2\n1 2\n1 2\n'),
    (((0, 0), (0, 0), (0, 0)), f'0 0\n0 0\n0 0\n'),
])
def test_print_matrix(data, result, capfd):
    matrix = usermatrix.get_object(tuple(data))
    capfd.readouterr()
    assert result == matrix.__str__()


@pytest.mark.parametrize("data1, data2, result", [
    (((1, 2), (1, 2), (1, 2)),
     ((1, 2), (1, 2), (1, 2)),
     f'2 4\n2 4\n2 4\n'),
    (((0, 0), (0, 0), (0, 0)),
     ((1, 2), (1, 2), (1, 2)),
     f'1 2\n1 2\n1 2\n'),
    (((0, 0, 1), (0, 0, 1), (0, 0, 2)),
     ((1, 2, 1), (2, 2, 1), (2, 2, 2)),
     f'1 2 2\n2 2 2\n2 2 4\n'),
    (((1,), (1,), (1,)),
     ((2,), (2,), (2,)),
     f'3\n3\n3\n'),
    (((1, 2),),
     ((2, 3),),
     '3 5\n'),
])
def test_add_matrices_correct(data1, data2, result):
    matrix1 = usermatrix.get_object(tuple(data1))
    matrix2 = usermatrix.get_object(tuple(data2))
    assert result == (matrix1 + matrix2).__str__()


@pytest.mark.parametrize("data1, data2", [
    (((1, 2), (1, 2), (1, 2)),
     ((1, 2), (1, 2), (1, 2), (1, 2))),
    (((0, 0, 1), (0, 0, 1), (0, 0, 2)),
     ((1, 2), (2, 2), (2, 2))),
    (((1, 2, 3),),
     ((1,), (2,), (3,))),
])
def test_add_matrices_of_diff_sizes(data1, data2):
    matrix1 = usermatrix.get_object(tuple(data1))
    matrix2 = usermatrix.get_object(tuple(data2))
    try:
        sum = matrix1 + matrix2
        assert False
    except matrix_exception.BadMatrixException:
        assert True


@pytest.mark.parametrize("data1, data2, result", [
    (((0, 0), (0, 0), (0, 0)),
     ((0, 0), (0, 0), (0, 0)),
     True),
    (((0, 0, 1), (0, 0, 1), (0, 0, 2)),
     ((1, 2, 1), (2, 2, 1), (2, 2, 2)),
     f'2 2 2\n2 2 2\n4 4 4\n'),
    (((1,), (1,), (1,)),
     ((2,), (2,), (2,)),
     f'6\n'),
    (((1, 2),),
     ((2,), (3,)),
     '8\n'),
])
def test_mul_matrices(data1, data2, result):
    matrix1 = usermatrix.get_object(tuple(data1))
    matrix2 = usermatrix.get_object(tuple(data2))
    try:
        mul = (matrix1 * matrix2).__str__()
        assert mul == result
    except matrix_exception.BadMatrixException:
        assert result
