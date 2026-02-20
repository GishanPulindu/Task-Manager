import json

print("---Welcome To My Task Manager---")
print("""Choose from below commands to run
add    - To create a task
view   - To view all tasks
up     - To update a task
del    - To delete a task
exit   - to exit the program""")


try:
    with open("Task.json", "r") as f0:
        tasks = json.load(f0)
        if tasks:
            print("--Available Tasks--")
            for i in tasks:
                print(i)
        else:
            print("No tasks yet.")
except FileNotFoundError:
    with open("Task.json", "w") as f0:
        add = []
        json.dump(add, f0, indent=4)


def create_task(t):
    task = {}
    with open("Task.json", "r") as f1:
        data = json.load(f1)
        if data:
            new_id = max(j["id"] for j in data) + 1
        else:
            new_id = 1
        task["id"] = new_id
        task["title"] = t
        task["completed"] = False
        data.append(task)
    with open("Task.json", "w") as f1:
        json.dump(data, f1, indent=4)
        print("Task created successfully!")
    return


def view_task():
    with open("Task.json", "r") as f2:
        data = json.load(f2)
        for j in data:
            print(j)
    return


def update_task(u):
    found = False
    with open("Task.json", "r") as f3:
        data = json.load(f3)
        for j in data:
            if j["id"] == u:
                print("""Choose from following
                title    - To update title
                done     - To complete a task""")

                update = input("Update title or complete task : ")
                if update.lower() == "title":
                    new_title = input("Enter new title: ")
                    j["title"] = new_title
                    found = True
                elif update.lower() == "done":
                    j["completed"] = True
                    found = True
                else:
                    print("Enter a valid update command!")
        if found:
            print("Task updated successfully!")
        else:
            print("Task Id not found!")
    with open("Task.json", "w") as f4:
        json.dump(data, f4, indent=4)
    return


def del_task(u):
    found = False
    with open("Task.json", "r") as f5:
        data = json.load(f5)
        for j in data:
            if j["id"] == u:
                data.remove(j)
                found = True
                break
        if found:
            print("Task deleted successfully!")
        else:
            print("Task Id not found!")
    with open("Task.json", "w") as f6:
        json.dump(data, f6, indent=4)
    return


while True:
    command = input("Enter a command to run: ")
    if command.lower() == "add":
        title = input("Add a title for the task: ")
        if title:
            create_task(title)
        else:
            print("Task title cannot be blank!")
    elif command.lower() == "view":
        view_task()
    elif command.lower() == "up":
        try:
            unique = int(input("Enter task id: "))
            if unique:
                update_task(unique)
            else:
                print("Entering a task id is mandatory!")
        except ValueError:
            print("Enter a valid number!")
    elif command.lower() == "del":
        try:
            unique = int(input("Enter task id: "))
            if unique:
                del_task(unique)
            else:
                print("Entering a task id is mandatory!")
        except ValueError:
            print("Enter a valid number!")
    elif command.lower() == "exit":
        break
    else:
        print("Enter a valid Command!")
