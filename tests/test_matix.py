from Lesson03.hw03_02 import Matrix
import pytest


@pytest.mark.parametrize("data_matrix1, data_matrix2, exam_res", [
    (
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],

            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],

            [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]],
    ),
    (
            [[2, 2, 2],
             [-1, -1, -1],
             [12, 12, 12]],

            [[-1, 1, 1],
             [1, 0, 1],
             [1, 1, 7]],

            [[1, 3, 3],
             [0, -1, 0],
             [13, 13, 19]],
    ),
])
def test_matrix_add_func(data_matrix1, data_matrix2, exam_res):
    res_matrix = Matrix(data_matrix1) + Matrix(data_matrix2)
    assert res_matrix.matrix == Matrix(exam_res).matrix
