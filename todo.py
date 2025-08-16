
def view():
    with open("todo.txt","r")as file:
        task=file.readlines()
        for index,data in enumerate(task,start=1):
            print(f"{index}:{data.strip()}")
    
def add():
    choice=(input("Enter the task desc: "))
    with open("todo.txt","a")as file:
        file.write(choice+"\n")


def completed():
    with open("todo.txt","r")as file:
        tasks=file.readlines()
        comp=int(input("Enter the number of completed task: "))
        if 0<comp<=len(tasks):
            tasks[comp-1]=tasks[comp-1].strip()+"[Done]\n"
        else:
            print("Invalid")
            return
    with open("todo.txt","w")as file:
        file.writelines(tasks)
    

def delete():
    with open("todo.txt","r")as file:
        tasks=file.readlines()
        rem=int(input("Which number should be deleted"))
        del tasks[rem-1]
    with open("todo.txt","w")as file:
        file.writelines(tasks)




print("To-Do List")
print("1.View Tasks")
print("2.Add task")
print("3.Mark task as completed")
print("4.Delete task")

inputo=int(input("Enter the task number:"))
if inputo==1:
    view()
elif inputo==2:
    add()
elif inputo==3:
    completed()
elif inputo==4:
    delete()
else:
    print("Enter a valid number")

