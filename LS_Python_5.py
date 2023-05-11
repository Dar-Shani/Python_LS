print("[26] - рекурсия\n[28] - Сжатие")
number = input("Выберите задание: ")

#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.
#*Пример:* A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8 

def Recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * Recursive(a, b - 1)

if number == "26":
    numberA = int(input("Введите число A: "))
    numberB = int(input("Введите число B: "))

    print(f"Итого {Recursive(numberA, numberB)}")

#Задача 28: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB ->
# -> A4B3C2XYZD4E3F3A6B28

def Rle(text_a, enum):
    enumeration = "" 
    count = 0;
    text_a += "."

    for a in range(len(text_a)):
        if enum == text_a[a]:
            count += 1
            
        if enum != text_a[a] and count > 1:
            enumeration += enum + str(count)
            count = 1
            enum = text_a[a]
        
        if enum != text_a[a] and count == 1:
            enumeration += enum
            count = 1
            enum = text_a[a]

    print(enumeration)

if number == "28":
    textA = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    Rle(textA, textA[0])
   
    
