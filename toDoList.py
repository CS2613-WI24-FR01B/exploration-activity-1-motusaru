import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        #add button
        add_button = tk.Button(root, text="Add Task", width=10, command=self.add_task, bg = 'light blue')
        add_button.pack(side=tk.LEFT, padx=5)

        #due date button
        due_date_button = tk.Button(root, text="Due Date", width=10, command=self.add_due_date, bg='red')
        due_date_button.pack(side=tk.LEFT, padx=5)

        #category button
        category_button = tk.Button(root, text="Category", width=10, command=self.select_category, bg='orange')
        category_button.pack(side=tk.LEFT, padx=5)

        #complete button
        complete_button = tk.Button(root, text="Complete Task", width=15, command=self.complete_task, bg='light green')
        complete_button.pack(side=tk.LEFT, padx=5)

        #frame for the listbox and scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10)

        #listbox to display tasks
        self.listbox = tk.Listbox(list_frame, width=50, height=10, bg='light pink')
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        #scrollbar for the listbox
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

    def add_task(self):
        task = self.entry.get()
        if task:
            due_date = ""
            category = ""
            self.tasks.append((task, due_date, category))  # task, due_date, category
            self.listbox.insert(tk.END, f"{task} (Due: {due_date}, Category: {category})")
            self.entry.delete(0, tk.END)

    def add_due_date(self):
        try:
            index = self.listbox.curselection()[0]
            due_date = simpledialog.askstring("Input", "Enter due date (YYYY-MM-DD):")
            if due_date:
                task, _, category = self.tasks[index]
                due_date_text = self.get_due_date_text(due_date)
                self.tasks[index] = (task, due_date_text, category)
                self.listbox.delete(index)
                self.listbox.insert(index, f"{task} (Due: {due_date_text}, Category: {category})")
        except IndexError:
            pass

    def get_due_date_text(self, due_date):
        try:
            due_date_dt = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_dt < datetime.now():
                return "Passed Due Date"
            else:
                return due_date
        except ValueError:
            return due_date

    def select_category(self):
        try:
            index = self.listbox.curselection()[0]
            category = simpledialog.askstring("Input", "Enter category:")
            if category:
                task, due_date, _ = self.tasks[index]
                self.tasks[index] = (task, due_date, category)
                self.listbox.delete(index)
                self.listbox.insert(index, f"{task} (Due: {due_date}, Category: {category})")
        except IndexError:
            pass

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            del self.tasks[index]
            self.listbox.delete(index)
            messagebox.showinfo("Completed", f"Task '{task}' has been completed!")
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
