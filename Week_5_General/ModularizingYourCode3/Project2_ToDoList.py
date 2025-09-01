#TO DO LIST

"""
Add tasks to an empty list
Remove a particular task when it has been completed and print the remaining and completed tasks 
Define a function for adding, viewing and removing
"""
import os
from pathlib import Path
file_path = Path.cwd() / "To_Do_List.txt"

tasks = []

#Adding tasks
def add_task(task):

    while True:
        try:
            task = input("\nPlease input a task: ")
            tasks.append(task)
            

            ends = input("Type 'end' to stop the program or Click Enter to skip: ").lower()
            if ends == "end":
                print(f"{len(tasks)} tasks added.")
                break
            else:
                pass


        except Exception:
            print("Invalid input, try again.")
            continue
    with open(file_path, "a", newline= "", encoding= "utf-8") as  f:
        f.writelines(tasks)



#Removing tasks
def remove_task(item):
    item = input("\nPlease input the completed task: ")
    if item in tasks:
        tasks.remove(item)
        print(f"Task {item} removed!")
        print(f"You have the following tasks left {tasks}")
    else:
        print("This task has not been added, try again.")

#Viewing tasks
def view_task():
    if tasks != "":
        print("To-Do List".center( 50, "."))
        for index, i in enumerate(tasks, 1):
            print(f"{index}.\t{i}")
    
    else:
        print("You do not have any task")
    with open(file_path, "r", newline= "", encoding= "utf-8") as  f:
        f.read()


#Accepitng user input

while True:
    option = input("\nChoose any of the following options: \n1. Add tasks \n2. Remove tasks \n4. View To-Do List \n4. Exit the program.: ").strip()

    if option == "1":
        print(add_task(tasks))

    elif option == "2":
        print(remove_task(tasks))

    elif option == "3":
        print(view_task())
    else:
        print("Invalid option, try again!")
        break
