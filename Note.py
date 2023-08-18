import View
import Model


View.functionReference()
isModifyNote = False

id = Model.idReconciliation()

command = input("command: ").split()
while command[0] != "exit":
    
    if command[0] == "add":
        View.clearConsole()
        Model.saveNote(Model.addNote(command[1], id), 'a')
        id += 1
        isModifyNote = False
    
    elif command[0] == "list":
        View.clearConsole()
        listNotes = []
        listNotes = (View.allShowNotes())
        isModifyNote = True
        command.clear

    elif command[0] == "sort" and isModifyNote == True:
        View.clearConsole()
        View.sortedList(listNotes)
        command.clear
    
    elif command[1].isdigit() and int(command[1]) <= id and isModifyNote == True:
    
        if command[0] == "show":
            View.clearConsole()
            print("Open ", listNotes[int(command[1])][1] +"\tВремя ", listNotes[int(command[1])][2] + "\n")
            print(listNotes[int(command[1])][3])
            command.clear

        elif command[0] == "edit":
            View.clearConsole()
            listNotes[int(command[1])] = Model.addNote(listNotes[int(command[1])][1], listNotes[int(command[1])][0]) 
            Model.updatingData(listNotes)
            command.clear
        
        elif command[0] == "del":
            View.clearConsole()
            del listNotes[int(command[1])]
            listNotes = Model.updatingId(listNotes)
            Model.updatingData(listNotes)
            command.clear
    
    else:
        print("Введена некоректная или не доступная команда")
    command = input("command: ").split()

    
        

    

    
