
import random
lst = [random.randint(-10,10) for i in range(10)]
for i in lst[:]:
    if i<0:
        lst.remove(i)
print (lst)

def udalenie(n,spisok):
    for i in range(len(spisok)):
        if len(spisok)!= n:
            spisok.pop() #удаляем все элементы после n



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