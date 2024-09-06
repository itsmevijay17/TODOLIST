tasks = []
from tkinter import *
from tkinter.ttk import *
from time import strftime
 
# creating tkinter window
root = Tk()
 
# Adding widgets to the root window
Label(root, text = 'TO DO LIST APP!!', 
      font =('Verdana', 15)).pack(side = TOP, pady = 10)
 
Button(root, text = 'SUBMIT!').pack(side = BOTTOM)
 
mainloop()

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    Label(master,"Task added successfully")

def listTasks():
    if not tasks:
        print("There are no tasks")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} is deleted successfully!")
        else:
            print("Task number not found")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    print("Welcome to my first app!")
    while True:
        print("\n")
        print("Please select one of the following operations:")
        print("#########################################")
        print("1. ADD A TASK")
        print("2. DELETE A TASK")
        print("3. LIST TASKS")
        print("4. QUIT")

        choice = input("ENTER A VALID CHOICE: ")
        if choice == '1':
            addTask()
        elif choice == '2':
            deleteTask()
        elif choice == '3':
            listTasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
