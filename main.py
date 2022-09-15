#                               Exercise 5: Health Management System

"""
Rules of using this code is:
1. You have to make a HMS folder in the python file folder where all the files will store.
2. Your file will save as, the name of client use and the type eg.- client = ramesh, type = food, file name
    will be rameshfood
3. All the operation on the file will be perfomed only if the name of file is correct.
4. Code will search the file in HMS folder, if you want different folder change the loc.
5. Whenever you want to do anything on a file, if it not exist you have to creat it first.
6. You are ready to use this code, Have a happy output, Thanks to use my code.
7. By Gopal singh
"""


#Mudules used
import os
import datetime

x = str(datetime.datetime.now())
y = ":\t"
z = "\n"

#----------------------------------------------Home page----------------------------------------------------------
print("\t\t\t\t\t\t\t\t\t\t\tWelcome to the health management system\n")
print("1. Press 0 for existing client.\n2. Press 1 for new client.\n3. Press 2 for delete a file.")
home = int(input())


if home == 1:
#-------------------------------------------New client page-------------------------------------------------------

    print("\t\t\t\t\t\t\t\t\t\t\tWelcome to the new client")
    print("Enter the name of New Client: ", end=""),
    new_name = input()
    print("Which file do you want to create: \n1. Food\n2. Workout\n")
    new_file = input()

    if new_file == "Food" or new_file == "food":
        if os.path.exists("HMS/" + new_name + new_file + ".txt"):
            print("This name file is already exist.")
        else:
            f1 = open("HMS/"+ new_name + new_file +".txt","x")
            print(new_name, " Your food file is created succesfully.")
            print("\nYour file name is: ", new_name + new_file)
            f1.close()

    elif new_file == "Workout" or new_file == "workout" or new_file == "work":
        if os.path.exists("HMS/" + new_name + new_file + ".txt"):
            print("This name file is already exist.")
        else:
            f1 = open("HMS/" + new_name + new_file + ".txt", "x")
            print(new_name, " your workout file is created succesfully.")
            print("\nYour file name is: ", new_name + new_file)
            f1.close()

    else:
        print("Enter correct file type")


elif home == 0:
#-------------------------------------Existing client page--------------------------------------------------------

    print("\t\t\t\t\t\t\t\t\t\t\tWelcome to Existing client")
    print("Enter the file name: ", end=""),
    file_search = input()
    if os.path.exists("HMS/"+file_search+".txt"):
        print(file_search, "File is found")
        print("\nYou can perform three operation on this file.\n1. Log new data: New\n2. Add data: Add\n3. Retrive data: Retrive")
        print("\nWhat you want to do with that file: ", end="")
        opr = input()
        if opr == "New" or opr == "new":
            print("Feed data in the file ", file_search)
            f = open("HMS/"+file_search+".txt", "w")
            f.write(x)
            f.write(y)
            f.write(input())
            f.close()

        elif opr == "Add" or opr == "add":
            again = "yes"
            while(again != "no"):
                print(file_search, " data : ")
                f = open("HMS/" + file_search + ".txt", "a")
                f.write(z)
                f.write(x)
                f.write(y)
                f.write(input())
                print("Do you want to write another line\nPress yes or no ", end="")
                again = input()
                f.close()

        elif opr == "Retrive" or opr == "retrive":
            print("Data in file: ", file_search)
            f = open("HMS/" + file_search + ".txt", "r")
            lines = len(f.readlines())
            print("\nTotal number of lines in this file is: ", lines, "\n")
            f.close()
            f = open("HMS/" + file_search + ".txt", "r")
            for read in range(lines):
                print(f.readline(), end="")
            f.close()

        else:
            print("Please select correct operation")

    else:
        print("File not found")


elif home == 2:
#--------------------------------------Delete file----------------------------------------------------------------

    print("Delete file:\n")
    print("Enter the name of the file: ",  end=""),
    delete_file = input()
    if os.path.exists("HMS/"+delete_file+".txt"):
        print("File has been found")
        os.remove("HMS/"+delete_file+".txt")
        print("File has been succesfully deleted")
    else:
        print("File does not exist")

else:
    print("Please enter correct a key")