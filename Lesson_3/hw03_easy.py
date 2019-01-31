'''
import random
lst = [random.randint(-10,10) for i in range(10)]
for i in lst[:]:
    if i<0:
        lst.remove(i)
print (lst)

<<<<<<< Updated upstream
def udalenie(n,spisok):
    for i in range(len(spisok)):
        if len(spisok)!= n:
            spisok.pop() #удаляем все элементы после n
=======
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
>>>>>>> Stashed changes

print (matrix)

<<<<<<< Updated upstream
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
=======
for line in matrix:
    print (line)
    
i=0
while len(matrix)>i:
    line = matrix[i]
    j=0
    while len(line)>j:
        print ('matrix[{}][{}] = {}'.format(i,j,matrix[i][j]))
        j+=1
    i+=1
>>>>>>> Stashed changes


for i ,line in enumerate(matrix):
    for j,el in enumerate(line):
        print ('matrix[{}][{}] = {}'.format(i, j, matrix[i][j]))

print (9 and 5 or 0)

d = {'name':'имя'}
if d.get('name'):
    name = d['name']
else:
    name = 'безымянный'
print (name)

print (d.get('name') if d.get('name') else 'безымянный')


import random
lst=[]
for _ in range(10):
    lst.append(random.randint(-10,10))
print (lst)

lst_g = [random.randint(-10,10) for _ in range(10)]
print (lst_g)

lst_i =[input('введите элементы матрицы построчно: ').split() for _ in range(3)]
for i ,line in enumerate(lst_i):
    for j,el in enumerate(line):
        lst_i[i][j]=int(lst_i[i][j])
for line in lst_i:
    print (line)

'''
import re

string = 'this is a simple test message for test'
pattern1 = '^test'

print (re.match(pattern1,string) is None)
found = re.findall(r'test', string)
print (found)