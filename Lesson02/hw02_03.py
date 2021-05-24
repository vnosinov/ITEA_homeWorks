# Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список.
# Для объектов класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы
# на число и user-friendly вывода матрицы на экран.


class Matrix:
    def __init__(self, nested_list):
        self.matrix = nested_list

    def view_matrix(self):  # моя функция
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], '  ', end='')
            print()

    def __str__(self):  # функцию подсмотрел
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])


    def __add__(self, other):
        pass




if __name__ == '__main__':
    l1 = [[1, 2], [4, 5], [7, 8]]
    l2 = [[1, 1], [1, 1], [1, 1]]

    m1 = Matrix(l1)
    m1.view_matrix()
    print(m1.__str__())
