def tasks():
    l=[]
    while True:
        print("\n------To Do List------")
        print("1.Add The Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Mark task as done")
        print("5.Exit")

        choice=int(input("Enter the choice :"))

        if choice==1:
            print()
            n=int(input("How many tasks you want to add?\n"))
            for i in range(1,n+1):
                task=input("Enter the Task :")
                l.append({"Task": task, "Done":False})
                print("Task Added!")
        if choice==2:
            print()
            for index,task in enumerate(l):
                status ="Done" if task["Done"] else "Not Done"
                print(f"{index+1}.{task} - {status}")
        if choice==3:
            print()
            n=int(input("Enter which task you want to delete : "))
            if 1 <= n <= len(l):
                remove=l.pop(n-1)
                print(f"Task {remove} deleted successfully!")
            else:
                print("Invalid task number.")
        if choice==4:
            print()
            m = int(input("\nEnter the task number to mark as done: "))
            if 1 <= m <= len(l):
                l[m- 1]["Done"] = True
                print(f"Task '{l[m - 1]}' marked as done ✅")
            else:
                print("Invalid task number.")
        if choice==5:
            break
tasks()
print("Thank You!")
