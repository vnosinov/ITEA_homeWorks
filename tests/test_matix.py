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


@pytest.mark.parametrize("data_matrix1, data_matrix2, exam_res", [
    (
            [[3, 3, 3],
             [3, 3, 3],
             [3, 3, 3]],

            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],

            [[2, 2, 2],
             [2, 2, 2],
             [2, 2, 2]],
    ),
    (
            [[1, 1, 1],
             [2, 2, 2],
             [10, 10, 10]],

            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 7]],

            [[0, 0, 0],
             [1, 2, 1],
             [9, 9, 3]],
    ),
])
def test_matrix_sub_func(data_matrix1, data_matrix2, exam_res):
    res_matrix = Matrix(data_matrix1) - Matrix(data_matrix2)
    assert res_matrix.matrix == Matrix(exam_res).matrix


@pytest.mark.parametrize("data_matrix, num_mul, exam_res",[
    (
        [[1, 1, 1],
         [1, 2, 1],
         [1, 1, 1]],

        5,

        [[5, 5, 5],
         [5, 10, 5],
         [5, 5, 5]]
    ),
    (
        [[1, 1, 1],
         [2, 2, 2],
         [3, 3, 3]],

        2,

        [[2, 2, 2],
         [4, 4, 4],
         [6, 6, 6]]
    )

])
def test_matrix_mul_func(data_matrix, num_mul, exam_res):
    res_matrix = Matrix(data_matrix) * num_mul
    assert res_matrix.matrix == Matrix(exam_res).matrix


@pytest.mark.parametrize("data_matrix, num_div, exam_res",[
    (
        [[10, 10, 10],
         [10, 10, 10],
         [10, 10, 10]],

        5,

        [[2, 2, 2],
         [2, 2, 2],
         [2, 2, 2]]
    ),
    (
        [[4, 4, 4],
         [4, 8, 4],
         [8, 8, 8]],

        2,

        [[2, 2, 2],
         [2, 4, 2],
         [4, 4, 4]]
    )

])
def test_matrix_div_func(data_matrix, num_div, exam_res):
    res_matrix = Matrix(data_matrix) / num_div
    assert res_matrix.matrix == Matrix(exam_res).matrix

