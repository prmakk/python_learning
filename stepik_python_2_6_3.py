#Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки, которая выводит все позиции, 
#на которых встречается число xx в переданном списке lst.

#Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

#Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

array_of_data, num= [int(i) for i in input().split()], int(input())
if num not in array_of_data:
    print('Отсутствует')
else:
    for x in range(len(array_of_data)):
        if num == array_of_data[x]:
            print(x, end=' ')