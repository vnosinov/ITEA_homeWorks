# Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список.
# Для объектов класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы
# на число и user-friendly вывода матрицы на экран.


class Matrix:
    def __init__(self, nested_list):
        self.matrix = nested_list

    def __str__(self):  # функцию подсмотрел
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        result = Matrix(other)
        result.matrix = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                x = self.matrix[i][j] + other.matrix[i][j]
                temp.append(x)
            result.matrix.append(temp)
        return result

    def __sub__(self, other):
        result = Matrix(other)
        result.matrix = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                x = self.matrix[i][j] - other.matrix[i][j]
                temp.append(x)
            result.matrix.append(temp)
        return result

    def __mul__(self, number):
        result = Matrix(self.matrix)
        result.matrix = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                x = self.matrix[i][j] * number
                temp.append(x)
            result.matrix.append(temp)
        return result

    def __truediv__(self, number):
        if number == 0 :
            return print('Ошибка, деление на ноль')
        result = Matrix(self.matrix)
        result.matrix = []
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                x = self.matrix[i][j] / number
                temp.append(x)
            result.matrix.append(temp)
        return result


if __name__ == '__main__':
    l1 = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    l2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    m1 = Matrix(l1)
    m2 = Matrix(l2)
    print(f'Матрица1 \n{m1}')
    print(f'Матрица2 \n{m2}')
    print(f'Сложение \n{m1 + m2}')
    print(f'Вычитание \n{m1 - m2}')
    print(f'Умножение \n{m1 * 2}')
    print(f'Деление \n{m1 / 3}')
