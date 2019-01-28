# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def udalenie(n,spisok):
    for i in range(len(spisok)):
        if len(spisok)!= n:
            spisok.pop() #удаляем все элементы после n

def okruglenie(b,n,spisok):
    for i in b[2:len(b)]:
        k = int(i)
        spisok.append(k)
    if spisok[n] > 5:
        spisok[n - 1] = spisok[n - 1] + 1
        udalenie(n,spisok)
    else:
        udalenie(n,spisok)

def round_chislo(n):
    import random
    a = random.random()
    b = repr(a)
    spisok = []
    okruglenie(b,n,spisok)
    chislo = 0
    for i in range(len(spisok)):
        chislo = chislo + spisok[i] * (10 ** (len(spisok) - i - 1))
    chislo = chislo / (10 ** (len(spisok)))
    print ('начальное число','{:>35}'.format(b))
    print ('округленное до указанного знака ',chislo)

n = int(input('кол-во знаков после которых будет округление: '))
round_chislo(n)


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def udacha(bilet):
    bilet1 = []
    for i in bilet:
        i = int(i)
        bilet1.append(i)
    a = sum(bilet1[0:3])
    b = sum(bilet1[3:6])
    if a == b:
        c = 1
    else:
        c = 0
    return c
bilet = input('введите 6-значный номер билета: ')
if udacha(bilet) == 1:
    print ('вам повезло!')
else:
    print ('не повезло')



