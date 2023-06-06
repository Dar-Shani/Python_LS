import export_bz as exp
import os.path

def Add_baza(data):
    if os.path.isfile(data) != True: #Проверяем сущестование базы
        print(data, "не найден")
    else:
         with open(data, "r") as reading:
            for re in reading:
                exp.contact_list.append(re.replace("\n",""))
                print("импортируется:[", re.replace("\n",""), "]")
         exp.Add_list()