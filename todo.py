#from traitlets import default
def main():
    tasks=[]
    
    def todo_menu():
        print("\n=====To-do list=====")
        print("------------")
        print("1. Add Task")
        print("__________")
        print("2. View Task")
        print("__________")
        print("3. Mark as done")
        print("__________")
        print("4. Search for the task")
        print("__________")
        print("5.Delete a task")
        print("__________")
        print("6. Exit")
    
    def add_task():
        task= input("Enter the description:")
        tasks.append({"task":task,"done":False})
        print("--task added!--")
    
    def view_task():
        if not tasks:
            print("--No task available!--")
            return
        for index,task in enumerate(tasks):
            status="Done" if task["done"] else "Not Done"
            print(f"{index+1}. {task["task"]}-{status}")
    
    def mark_done():
        index=int(input("Enter the task number to be marked:"))-1
        if 0<=index<len(tasks):
            tasks[index]["done"]=True
            print("--Task marked as done!--")
        else:
            print("--Invalid task number--")
                
    def search_task():
        keyword = input("Enter keyworkd for the task:")
        found_task=[task for task in tasks if keyword.lower() in task["task"].lower()]
        if found_task:
            print("\nSearch Result:")
            for index,task in enumerate(found_task):
                status="Done" if task["done"] else "Not Done"
                print(f"{index+1}. {task['task']}-{status}")
    
        else:
            print("--Invalid Keyword--")
    def delete_task():
        try:
            index=int(input("Enter task number to be deleted:"))-1
            print("\n Search task to be deleted:")
            if 0<=index<len(tasks):
                deleted=tasks.pop(index)
                print(f"--Task {deleted['task']} has been deleted!--")
            else:
                print("--invalid task number--")
        except ValueError:
            print("--Entered a valid number--")
    while True:
        todo_menu()
        choice=int(input("Enter your choice:"))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            mark_done()
        elif choice==4:
            search_task()
        elif choice==5:
            delete_task()
        elif choice==6:
            print("--Exiting--")
            break
        else:
            print("==Invalid Choice. Please try again==")
            
if __name__=="__main__":
    main()