# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# import random
# n = int(input('Введите число:'))
# some_list = [random.randint(-n, n) for i in range(n)]
# print(some_list, ' -> на нечётных позициях элементы: ', end='')
# sum = 0
# for i in range(1, n, 2):
#     sum += some_list[i]
#     print(some_list[i], end=', ')
# print('ответ: ', sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# import random
# n = int(input('Введите число:'))
# some_list1 = [random.randint(-n, n) for _ in range(n)]
# print(some_list1, end = '')
# print(' => ',[some_list1[i] * some_list1[-1 * (1 + i)] for i in range(0, (n + 1) //2)])

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

# import random
# n = int(input())
# some_list = [round(random.randint(1,19) + random.random(),2) for _ in range(n)]
# print(some_list, end = '')
# some_list2 = [i%1 for i in some_list if i%1 != 0]
# print(' =>', round((max(some_list2) - min(some_list2)), 2))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число:'))
# new_str = ' ' 
# while n > 0:  
#     new_str = new_str + str(n % 2)  
#     n = n // 2
# for i in reversed(new_str):
#     print(i, end = '')

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input("Введите размер числа Фибоначчи: "))
if n < 0: n = n*-1
f1 = f2 = 1
list1 = [f1, f2]
for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list1.append(f2)
print(list1)
f1=f2=1
for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list1.insert(0, f2)
print(list1)