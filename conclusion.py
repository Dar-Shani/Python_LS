import os.path

def demonstration(data):
    count = 0 #счётчик
    if os.path.isfile(data) != True: #Проверяем сущестование базы
        print(data, "не найден")
    else:
        with open(data, "r") as reading:
            for re in reading:
                count += 1
                print(count,": ", re.replace("*"," "), end="")