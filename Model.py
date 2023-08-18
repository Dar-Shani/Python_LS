import csv
import datetime
import os


def idReconciliation():
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            id = 0
            for i in reader:
                id = int(i[0])
        return id + 1
    else:
        return 0
    

def recordingTime():
    time = datetime.datetime.now()
    return time.strftime('%Y-%m-%d %H:%M')

def addNote(introduction, id):
    content = [id]
    content.append(lengthCheck(introduction))
    content.append(" " + recordingTime())
    content.append(input("Текст заметки: "))
    print("Save Note")
    return content

def lengthCheck (text):
    if len(text) < 20:
        textA = text + " " * (20 - len(text))
    elif len(text) > 20:
        textA = text[:20]
    else:
        textA = text
    return textA


def saveNote(listText, mode):
    with open('data.csv', mode, newline='') as file:
        writer = csv.writer(file)
        writer.writerow(listText)

def updatingData(list):
    for i in range(len(list)):
            if i == 0:
                saveNote(list[i], 'w')
            else:
                saveNote(list[i], 'a')

def updatingId(list):
    for i in range(len(list)):
        list[i][0] = i
    return list


