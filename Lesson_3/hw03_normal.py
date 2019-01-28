# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachi(n,m):
    fibonchi1 = [1, 1]
    i = 2
    while i < m:
        k = fibonchi1[i - 2] + fibonchi1[i - 1]
        fibonchi1.append(k)
        i = i + 1
    return fibonchi1[n-1:m]
n = int(input('введите индекс первого элемента последовательности: '))
m = int(input('введите индекс последнего элемента последовательности: '))
print (fibonachi(n,m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random
def sortirovka(spisok):
    n = 1
    while n < len(spisok):
        for i in range(len(spisok) - n):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
        n = n + 1
    return spisok

spisok=[]
for i in range(0,20):
    k=random.randint(0,99)
    spisok.append(k)
print ('случайный список:')
print (spisok)
print ('отсортрованный список:')
print (sortirovka(spisok))

#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math
def dlina(x1,x2,y1,y2):
    ras = math.sqrt(((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2))
    return ras
a1=input('введите x1 и y1 через пробел').split()
a2=input('введите x2 и y2 через пробел').split()
a3=input('введите x3 и y3 через пробел').split()
a4=input('введите x4 и y4 через пробел').split()
a= dlina(a1[0],a2[0],a1[1],a2[1])
b=  dlina(a2[0],a3[0],a2[1],a3[1])
d1=dlina(a1[0],a3[0],a1[1],a3[1])
d2=dlina(a2[0],a4[0],a2[1],a4[1])
if (d1**2) + (d2**2) == 2*((a**2)+(b**2)):
    print('параллелограмм')
else:
    print ('не параллелограмм')

