import tkinter
from tkinter import ttk
from tkinter import messagebox
import json

def gui_run():

    def refresh_list(data):
        tasks_listbox.delete(0, tkinter.END)

        for task in data:
            display = f"ID: {task['id']} |Title: {task['title']} |Difficulty: {task['difficulty']} |Completed: {task['completed']}"
            tasks_listbox.insert(tkinter.END, display)


    def add_task():
        title = title_entry.get()
        diff = selected_difficulty.get()

        if not title or title == "--Title of the Task--":
            messagebox.showerror("Error", "Title of the Task is required")
            return

        with open("Task.json", "r") as f1:
            data = json.load(f1)
            if data:
                new_id = max(j["id"] for j in data) + 1
            else:
                new_id = 1

            task = {"id": new_id, "title": title, "difficulty": diff, "completed": False}
            data.append(task)

        with open("Task.json", "w") as f2:
            json.dump(data, f2, indent=4)

        new_task = f"ID: {task['id']} |Title: {task['title']} |Difficulty: {task['difficulty']} |Completed: {task['completed']}"
        tasks_listbox.insert(tkinter.END, new_task)

        title_entry.delete(0, tkinter.END)
        title_entry.insert(0, "--Title of the Task--")
        dropdown.current(0)


    def update_task():
        selected = tasks_listbox.curselection()
        title = title_entry.get()
        if not selected:
            messagebox.showerror("Error", "No tasks selected")
            return
        elif not title or title == "--Title of the Task--":
            messagebox.showerror("Error", "Title of the Task is required")
            return

        index = selected[0]
        with open("Task.json", "r") as f1:
            data = json.load(f1)

            data[index]["title"] = title_entry.get()
            data[index]["difficulty"] = selected_difficulty.get()

        with open("Task.json", "w") as f2:
            json.dump(data, f2, indent=4)

        refresh_list(data)

        title_entry.delete(0, tkinter.END)
        title_entry.insert(0, "--Title of the Task--")
        dropdown.current(0)


    def complete_task():
        selected = tasks_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No tasks selected")
            return

        index = selected[0]
        with open("Task.json", "r") as f1:
            data = json.load(f1)

            data[index]["completed"] = not data[index]["completed"]

        with open("Task.json", "w") as f2:
            json.dump(data, f2, indent=4)

        refresh_list(data)


    def delete_task():
        selected = tasks_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No tasks selected")

        index = selected[0]
        with open("Task.json", "r") as f1:
            data = json.load(f1)

            del data[index]

        with open("Task.json", "w") as f2:
            json.dump(data, f2, indent=4)

        refresh_list(data)


    root = tkinter.Tk()
    root.title("Task Manager")
    root.geometry("500x600")

    difficulty = ["Easy", "Medium", "Hard"]
    selected_difficulty = tkinter.StringVar()
    selected_difficulty.set(difficulty[0])

    title_entry = ttk.Entry(root, font=("Arial", 15), width=35)
    title_entry.grid(row=0, column=0, columnspan=1)

    title_entry.insert(0, "--Title of the Task--")

    dropdown = ttk.Combobox(root, font=("Arial", 15), width=32, textvariable=selected_difficulty, values=difficulty, state="readonly")
    dropdown.grid(row=1, column=0, columnspan=1)

    add_button = tkinter.Button(root, text="Add Task", font=("Arial", 15), relief="raised", command=add_task)
    add_button.grid(row=0, column=2, rowspan=2)

    complete_button = tkinter.Button(root, text="Complete Task", font=("Arial", 15), relief="raised", command=complete_task)
    complete_button.grid(row=2, column=0, columnspan=3, rowspan=2)

    tasks_listbox = tkinter.Listbox(root, font=("Arial", 15), relief="sunken")
    tasks_listbox.grid(row=5, column=0, columnspan=3, rowspan=13, sticky="nsew")

    update_button = tkinter.Button(root, text="Update Task", font=("Arial", 15), relief="raised", command=update_task)
    update_button.grid(row=18, column=0, columnspan=3, rowspan=1, sticky="nsew")

    delete_button = tkinter.Button(root, text="Delete Task", font=("Arial", 15), relief="raised", command=delete_task)
    delete_button.grid(row=19, column=0, columnspan=3, rowspan=1, sticky="nsew")

    for i in range(20):
        root.rowconfigure(i, weight=1)
    for i in range(3):
        root.columnconfigure(i, weight=1)

    try:
        with open("Task.json", "r") as f0:
            tasks = json.load(f0)
            if tasks:
                for i in tasks:
                    new = f"ID: {i['id']} |Title: {i['title']} |Difficulty: {i['difficulty']} |Completed: {i['completed']}"
                    tasks_listbox.insert(tkinter.END, new)
    except FileNotFoundError:
        with open("Task.json", "w") as f0:
            add = []
            json.dump(add, f0, indent=4)

    root.mainloop()


if __name__ == "__main__":
    gui_run()