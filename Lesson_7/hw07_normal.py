'''
Задача-1: Создать класс Матрица. В конструктор класса передавать переменную
содержащую матрицу в виде списка списков. В конструкторе класса преобразовать
список списков в привычный матричный вид. Переопределить стандартное поведение
методов __add__ и __str__ класса. Создать два экземпляра класса Матрица с данными.
Метод __add__ должен реализовывать сложение матриц, а __str__ - вывод итоговой
матрицы.
'''
class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix

    def __add__(self, other):
        for _ in range(len(self.matrix)):
            for __ in range(len(other.matrix)):
                self.matrix[_][__] = self.matrix[_][__] + other.matrix[_][__]

    def __str__(self):
        m = ''
        for _ in self.matrix:
            m = m + str(_).replace(',', '').replace('[', '').replace(']', '') + '\n'
        return m

matrix1 = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
matrix2 = Matrix([[16,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]])
matrix1.__add__(matrix2)
print(matrix1)
