tasks = ['Complete Python project', 'Review pull requests']

def printSeparator():
    # Print a separator line.
    print("=" * 160)

def printMeerkat():
    # Print ASCII art of a meerkat.
    print(r"""
      /\_/\  
     ( o.o ) 
      > ^ <
    """)

printSeparator()
printMeerkat()
print(f"Welcome to ToDo App | You have {len(tasks)} Tasks")
printSeparator()

def entryCommand():
    # Display the main menu and handle user input.
    printSeparator()
    x = str(input("Input Command | Add Task | View Tasks | Delete Task | Quit? "))
    try:
        if x == "Add Task":
            addTaskCommand()
        elif x == "View Tasks":
            viewTaskCommand() 
        elif x == "Delete Task":
            deleteTaskCommand()
        elif x == "Quit":
            quitCommand()
        else:
            raise ValueError("Unknown Command")
    except ValueError as e:
        print(e)
        entryCommand()

def addTaskCommand():
    # Add a new task to the task list.
    printSeparator()
    print("Add Task Command Executed")
    taskInput = input("Enter Your Task: ").strip()
    if taskInput:
        print("Task has been added!")
        tasks.append(taskInput)
        entryCommand()
    else:
        print("Invalid Input, try again")
        addTaskCommand()

def viewTaskCommand():
    # View all tasks in the task list.
    printSeparator()
    print("View Task Command Executed")
    if len(tasks) <= 0:
        print("You have no tasks!")
        entryCommand()
    else:
        print(f'Total Tasks: {len(tasks)}')
        for i in range(len(tasks)):
            print(f'Task {i + 1}: {tasks[i]}')
            printSeparator()
        entryCommand()

def deleteTaskCommand():
    # Delete a task from the task list.
    printSeparator()
    print("Delete Task Command Executed")
    if len(tasks) <= 0:
        print("You have no tasks to delete!")
        entryCommand()
    else:
        try:
            taskNumber = int(input("Enter Your Task Number to delete: ")) - 1
            if 0 <= taskNumber < len(tasks):
                tasks.pop(taskNumber)
                print("Task has been deleted!")
            else:
                print("Invalid Task Number, please try again")
                deleteTaskCommand()
        except ValueError:
            print("Invalid Input, please enter a number")
            deleteTaskCommand()
        entryCommand()  

def quitCommand():
    # Quit the application.
    printSeparator()
    print("Quit Command Executed")
    print("Have a good Day User!")
    input("Input Any Key To Start Task Manager")
    print(f'Welcome Back User! You have: {len(tasks)} Tasks')
    entryCommand()

entryCommand()
