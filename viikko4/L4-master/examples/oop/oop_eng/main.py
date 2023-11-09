#  This program processes files using the object-oriented program paradigm
# ---- Main Program Initialization ----

from menu import Menu


# Let´s define files
files = [ 'file1.txt', 'file2.txt', 'file3.txt' ]

# Let´s create object "menu" from the class Menu
menu = Menu(files)

# ---- Main Program starts ----
# ask the user for the selected file

A = True

while A == True:

    menu.fileSelect()
    menu.operationSelect()
    menu.operationRun()

    input = input("Select 1 to continue using program, select any other key to shut it down: ")
    try:
        if input == "1":
            del input 
            continue
        else:
            A = False
    except:
        A = False


# ---- Main Program ends ----
print("Shutting Down")