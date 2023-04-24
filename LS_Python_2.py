import random

print("[10] - монетки \n[12] - угадай числа \n[14] - степени двойки")
number = input("Выберите задание: ")

#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
#а некоторые – гербом. Определите минимальное число монеток, 
#которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же 
#стороной. Выведите минимальное количество монет, которые нужно перевернуть
if number == "10":
    
    coins = random.randint(10, 100)
    eagle = random.randint(0, coins)
    print(f"Дано:\nмонет - {coins}\nорёл  - {eagle}\nрешка - {coins - eagle}")
    print(f"Минимальное значение {min(eagle, coins - eagle)}")

#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
if number == "12":
    
    numberX = random.randint(1,1000)
    numberY = random.randint(1,1000)
    numberS = numberX + numberY
    numberP = numberX * numberY

    print(f"Петя загадал X - {numberX}, Y - {numberY}")
    print(f"Подсказал сумму чисел S - {numberS}\nИ их произведение P - {numberP}")

    break_out_flag = False
    for a in range(1000):
        for b in range(1000):
            if a + b == numberS and a * b == numberP:
                print (f"числа {a}, {b}")
                break_out_flag = True
                break
        if break_out_flag:
            break
    
 #Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
 # не превосходящие числа N.   
if number == "14":
    
    number = int(input("Выберите число N: "))
    stop = 0
    P = 2

    for i in range(number):
        if stop != 1:
            P = P ** i
            if P <= number:
                print(P, end=' ')
                P = 2
            else:
                stop = 1
        else:
            i = number