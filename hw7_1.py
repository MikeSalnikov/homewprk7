# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for row in self.list:
            for i in row:
                print(f"{i}", end=" ")
            print()
        return ''

    def __add__(self, other):
        for row in range(len(self.list)):
            for i in range(len(self.list[row])):
                self.list[row][i] = self.list[row][i] + other.list[row][i]
        return Matrix.__str__(self)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]])
m2 = Matrix([[2, 4, 6], [8, 10, 7], [6, 3, 1], [2, 4, 7]])
print(m1.__add__(m2))