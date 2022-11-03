def polindrom(n):
    la = []
    r = ''
    for i in n :
        la.append(i)
    la.reverse()
    for j in la:
        r += j

    if a ==r:
        print('Полиндром')
    else:
        print("Не полиндром")
print("текст")
a= input()
polindrom(a)
