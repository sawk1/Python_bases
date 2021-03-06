'''
Задача-1: Реализовать индексацию элементов списка не с нуля, а с 5, т.е. 5, 6, 7
и т.д.
'''
class IterObj:
    def __init__(self, start=0):
        self.i = start
    def __next__(self):
        self.i += 1
        if self.i <= 10:
            return self.i
        else:
            raise StopIteration

class Iter:
    def __init__(self, start=5):
        self.start = start - 1
    def __iter__(self):
        return IterObj(self.start)

lst = Iter()
for _ in lst:
    print(_)
'''
Задача-2: Придумать любу структуру данных. Она должна содержать два атрибута.
Значение одного атрибута передается в конструктор, а значение другого - определяетсяъ
прямо в конструкторе класса. Для этой структуры данных написать метод,
который должен выполнять какой-то функционал. Создать экземпляр класса, передать
данные. Вызывать метод. Проверить, что находится в переменной-экземпляре класса.
Переопределить метод __str__. Этот метод должен возвращать тот результат,
который вы захотите. Проверить еще раз. В комментарии написать, в чем разница
между подходом с использованием метода __str__ и без него.
'''
class NewClass:
    def __init__(self, n):
        self.n=n
    # выводим дробную часть числа
    def cel(self):
        return self.n - int(self.n)

    def  __str__(self):
        return f'целая часть {int(self.n)} и дробная часть {self.cel()}'

a = NewClass(12.3215)
drob=a.cel()
strok = str(a)
print(drob)
print(strok)
'''
Задача-3: Продолжить работу над задачей 2. Добавить еще один метод. Он должен
вывзваться из экземпляра класса. В этот метод нужно передать некое значение.
Сам метод должен ловить значение и что-то с ним делать и возвращать результат.
Реализовать для этого метода декоратор @staticmethod
'''

class NewClass:
    def __init__(self, n):
        self.n=n
    # выводим дробную часть числа
    def cel(self):
        return self.n - int(self.n)

    def  __str__(self):
        return f'целая часть {int(self.n)} и дробная часть {self.cel()}'

    @staticmethod
    def type2(drob):
        return type(drob)

a = NewClass(12.3215)
drob=a.cel()
strok = str(a)
type1=a.type2(drob)
print(type1)

