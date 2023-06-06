import os.path


def consider_contact(text):
    if os.path.isfile("file1.txt") != True: #Проверяем сущестование базы
        print("file1.txt", "не найден")
    else:
        with open("file1.txt", "r") as reading:
            print("Ищем\n")
            for re in reading:
                if text in re:
                    print(re.replace("*"," "))
                
