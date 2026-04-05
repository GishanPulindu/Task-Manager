# 📝 GUI Task Manager (Python + Tkinter)

A simple **Task Manager application with a graphical user interface (GUI)** built using Python and Tkinter.
This app allows users to create, update, complete, and delete tasks while storing data persistently using JSON.

---

## 🚀 Features

* ➕ Add new tasks with title and difficulty
* ✏️ Update existing tasks
* ✅ Mark tasks as completed / incomplete
* ❌ Delete tasks
* 💾 Persistent storage using `Task.json`
* 🖥️ User-friendly GUI built with Tkinter

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* JSON (data storage)

---

## 📂 Project Structure

```
.
├── CLI Task Manager.py        #If you want to check out my CLI version
├── GUI Task Manager.py        # Main application file
├── Task.json                  # Stores all tasks (auto-created)
└── GUI Readme.md              # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**

```
git clone https://github.com/your-username/gui-task-manager.git
cd gui-task-manager
```

2. **Run the application**

```
python GUI Task Manager.py
```

---

## 🧠 How It Works

* Tasks are stored as a list of dictionaries in a JSON file:

```
{
    "id": 1,
    "title": "Example Task",
    "difficulty": "Easy",
    "completed": false
}
```

* The GUI interacts with this file to:

  * Read tasks
  * Modify them
  * Save updates instantly

---

## ⚠️ Notes

* If `Task.json` does not exist, it will be created automatically.
* Ensure the file is not manually edited incorrectly (invalid JSON may cause errors).

---

## 🔥 Future Improvements

* Add search functionality
* Add task filtering (Completed / Pending)
* Improve UI design
* Use checkboxes instead of text for completion
* Add due dates and priorities

---

## 💡 What I Learned

* Building GUI applications using Tkinter
* Managing persistent data using JSON
* Handling user input and events
* Structuring a real-world Python project

---

## 📌 Version

**v1.0** – Basic GUI Task Manager with CRUD functionality

---

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome!

---

## 📜 License

This project is open-source and free to use.
