#Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

result = 0
def fx(x):
    if x <= -2:
        result = 1 - (x + 2)**2
        return result
    elif -2 < x <= 2:
        result = -x/2
        return result
    elif 2 < x:
        result = (x - 2)**2 + 1
        return result
