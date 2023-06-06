
import conclusion as con #вывод
import export_bz as exp  #сохранения
import import_bz as imp  #импорт
import search_contact    #поиск

command = None
print("1 Вывод списка данных \n2 Добавить в список \n3 Импорт \n4 Поиск\n")
number = 0 #номер для вывода и ввода.
while command != "Выход":
    
    command = input("команда: ")
    
    if command == "1":
        print("[№][Фамилия][Имя][Телефон][Описание]")
        con.demonstration("file1.txt")

    if command == "2":
        print("Режим редактирования " "\n" "Для выхода напишите стоп")
        print("[_][Фамилия][_][Имя][_][Телефон][_][Описание]")
        while command != "стоп":
            number += 1
            command = input(f" {number}: ")
            exp.contact_list.append(command.replace(" ", "*"))

        exp.contact_list.pop() #удаляем команду стоп
        exp.Add_list()

    if command == "3":
        command = input("Укажите имя или адрес файла для импорта данных \n")
        imp.Add_baza(command)
    
    if command == "4":
        print("Поиск зависит от регистра")
        command = input("Для поиска укажите фамилию, имя, тел, описание: ")
        search_contact.consider_contact(command)