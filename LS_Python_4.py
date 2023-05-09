import random

print("[22] - набор чисел\n[24] - черника")
number = input("Выберите задание: ")

#Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке возрастания 
# все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
def Count(_count, nm):
    while nm > 0:
        _count.add(input(f"Осталось {nm} добавить: "))
        nm -= 1


if number == "22":
    countN = set ()
    countM = set ()

    n = int(input("n: "))
    m = int(input("m: "))
    
    Count(countN, n)
    Count(countM, m)
    
    print(f"Данно\nN: {countN}\nM: {countM}")

    countC = countN.union(countM)

    print(f"После слияния {sorted(countC)}")

#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
# выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно 
# перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

def RandomCount(_list):
    for i in range(8):
        _list.append(random.randint(1,10))

if number == "24":
    berries = []
    berries_count = []
    RandomCount(berries)

    print(f"Данно 8 кустов, содержание ягод на всех кустах {berries}")
            
    for i in range(len(berries) - 1):
        berries_count.append(berries[i - 1] + berries[i] + berries[i + 1])
    berries_count.append(berries[-2] + berries[-1] + berries[0])

    print(max(berries_count))