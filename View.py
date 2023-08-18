import csv
import os

def functionReference():
    print("add plan - Ввести новую заметку, plan оглавление")
    print("exit     - выйти с программы")
    
    print("list     - показать все заметки")
    print("Следующие команды активны после list")
    print("sort     - сортировать, сперва старые")
    print("show 1   - показать заметку по id 1")
    print("edit 1   - редактировать заметку id 1")
    print("dell 1   - удалить заметку по id 1")


def allShowNotes():
    print("id \tОглавление \t\t Время")
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        listNotes = []
        for i in reader:
            listNotes.append(i)
            print(i[0] +"\t"+ i[1] + "\t" + i[2])
    print("Доступны комманды сортировать ,открыть, изменить, удалить")
    return listNotes

def sortedList(list):
    listS = sorted(list, key=lambda x: x[2])
    for i in listS:
         print(i[0] +"\t"+ i[1] + "\t" + i[2])

def clearConsole():
    osType = os.name
    if osType == "nt":
        os.system('cls')
    else:
        os.system('clear')

