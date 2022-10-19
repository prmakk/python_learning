#На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.

#Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.


with open('./dataset_3363_2 (3).txt', 'r') as out:
    str = out.readline().strip()
b = []
for i in range(len(str)):
    if str[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=str[i]
        str=str[:i]+"!"+str[i+1:]
c=str.split('!')[1:]
with open('text.txt', 'w') as ouf:
    for i in range(len(b)):
        ouf.write(b[i]*int(c[i]))
