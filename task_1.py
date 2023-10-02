def CreateList():
    work = input("Enter the name of your work : " )
    ToDoList.append(work)
def DisplayList(n):
    if n == 1:
        if len(ToDoList) == 0:
            print("List is empty\n")
        else:
            for i in range(len(ToDoList)):
                print(ToDoList[i])
    elif n == 2:
        if len(CompletedList) == 0:
            print("List is empty\n")
        else:
            for i in range(len(CompletedList)):
                print(CompletedList[i])
    elif n == 3:
        if len(StartedList) == 0:
            print("List is empty\n")
        else:
            for i in range(len(StartedList)):
                print(StartedList[i])
    else:
        print("No such list found")
ToDoList = []
CompletedList = []
StartedList = []
while True:
    print("Select the list which you want to work with : ")
    op = int(input("1.Create list\n2.To Do List\n3. Completed list\n4.Started list\n5.Display list\n6.Exit  : "))
    if op == 1:
        while True:
            ch = int(input("1.Insert data\n2.Exit from create list  : "))
            if ch == 1:
                CreateList()
            elif ch == 2:
                break
    elif op == 2:
        work = input("Enter the name of your work :")
        ToDoList.append(work)
    elif op == 3:
        work = input("Enter the name of your work : ")
        CompletedList.append(work)
        StartedList.remove(work)
    elif op == 4:
        work = input("Enter the name of your work : ")
        StartedList.append(work)
        ToDoList.remove(work)
    elif op == 5:
        n = int(input("1.To Do List\n2.Completed list\n3.Started list  : "))
        DisplayList(n)
    elif op == 6:
        exit()
    else:
        print("Choose correct option")

