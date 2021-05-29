from Lesson03.hw03_02 import Matrix
import pytest


def test_matrix_add_func():
    l1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    l2 = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    l3 = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    m1 = Matrix(l1)
    m2 = Matrix(l2)
    m3 = Matrix(l3)
    assert m1 + m2 == m3
