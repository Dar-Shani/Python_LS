



contact_list = []

def Add_list():
      
    with open("file1.txt", "a+") as bz_txt:
        for i in range(len(contact_list)):
            bz_txt.write(contact_list[i] + "\n")

    contact_list.clear() #чистим лист


