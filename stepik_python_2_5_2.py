#Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

#Если на вход пришло только одно число, надо вывести его же.

#Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.


s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:        #возращаем число, если оно единственное
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:                           #выводим новый массив после расчётов
        print(str(t[j])+' ',end='')
        j +=1
