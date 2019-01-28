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
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os
chasi,chasi1,zarplata,workers1,hours1,real_zp=[],[],[],[],[],[]
path_workers = os.path.join('data','workers')
workers = open(path_workers, 'r', encoding='UTF-8')
path_hours = os.path.join('data','hours_of')
hours = open(path_hours, 'r', encoding='UTF-8')
for line in workers:
    workers1.append(line.split())
for line in hours:
    hours1.append(line.split())
i=1
while i<=6:
    chasi.append(workers1[i][4])
    zarplata.append(workers1[i][2])
    chasi1.append(hours1[i][2])
    i=i+1
n=0
while n<6:
    k=int(zarplata[n])/int(chasi[n])
    if int(chasi[n])>int(chasi1[n]):
        z=int(chasi[n])-int(chasi1[n])
        f=int(int(zarplata[n]) - z*k)
        real_zp.append(f)
    elif int(chasi[n])<int(chasi1[n]):
        z = int(chasi1[n]) - int(chasi[n])
        f = int(int(zarplata[n]) + 2*z * k)
        real_zp.append(f)
    else:
        real_zp[n]=int(zarplata[n])
    n=n+1
itogo=sum(real_zp)
print (itogo)
workers.close()
hours.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os
all_fruits=[]
alfovit = list(map(chr, range(ord('А'), ord('Я')+1)))
path_fruits = os.path.join('data','fruits.txt')
fruits = open(path_fruits, 'r', encoding='UTF-8')
for line in fruits:
    all_fruits.append(line.split(' '))
    all_fruits.sort()
all_fruits=all_fruits[282:len(all_fruits)]
for n in range(len(alfovit)):
    with open('data/fruits_%s.txt' % (alfovit[n]), 'w', encoding='utf-8') as file:
        for i in all_fruits:
            a = ' '.join(i)
            if i[0][0] == alfovit[n]:
                file.write(a + '\n')
    if os.stat('data/fruits_%s.txt' % (alfovit[n])).st_size == 0:
        os.remove('data/fruits_%s.txt' % (alfovit[n]))