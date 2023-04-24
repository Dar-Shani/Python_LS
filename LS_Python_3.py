import random

print("[16] - количество повторов\n[18] - самый подходящий")
number = input("Выберите задание: ")

#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в списке A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

if number == "16":
    number = int(input("Укажите размер массива: "))
    listA = []
    countA = 0

    for i in range(number):
        listA.append(random.randint(0, number))
    print(f"Данно {listA}")
    
    number = int(input("Выберите число для подсчёта его повторов: "))

    for i in range(len(listA)):
        if number == listA[i]:
            countA += 1

    print(f"Число {number} повторов {countA}")

#Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в списке. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X

if number == "18":
    number = int(input("Укажите размер массива: "))
    listB = []
    countB = 0

    for i in range(number):
        listB.append(random.randint(0, number))
    print(f"Данно {listB}")

    number = int(input("Выберите число для поиска близких значений: "))

    for i in range(len(listB)):
        if number  == listB[i]:
            countB = listB[i]
            break
        if number - 1 == listB[i] or number + 1 == listB[i]:
            countB = listB[i]
    
    print(f"Число {number} найдено близкое значение {countB}")
        
