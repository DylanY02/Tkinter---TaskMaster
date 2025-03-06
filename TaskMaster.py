from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

task_list = []

def add_task():
    task = entry_task.get()
    if task:
        task_list.append(task)
        task_box.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning("Entrez une tâche")

def validate_task():
    try:
        selected_index = task_box.curselection()[0]
        selected_task = task_box.get(selected_index)
               
        if not selected_task.endswith(" ✓"):
            validated_task = selected_task + " ✓"  
            task_box.delete(selected_index)  
            task_box.insert(selected_index, validated_task)  
            task_box.itemconfig(selected_index, {'fg': 'green'}) 
        else:
            messagebox.showinfo("Information", "Task already validated.")
    except IndexError:
        messagebox.showwarning
        
def delete_task():
    try:
        selected_index = task_box.curselection()[0]
        task_box.delete(selected_index)
        del task_list[selected_index] 
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        

#Créer la fenêtre principale
root = Tk()
root.title("Gestionnaire de tâches")

#Contient et organise les widgets
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0)

#Permet à la fenêtre de s'agrandir et de se centrée
frame_input.grid_rowconfigure(1, weight=1)
frame_input.grid_columnconfigure(0, weight=1)
frame_input.grid_columnconfigure(1, weight=1)

#Permet à la fenêtre d'être redimensionnée
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#Labelbox où l'utilisateur entre la tâche
entry_task = ttk.Entry(frame_input, width=40)
entry_task.grid(row=0, column=0, padx=5, pady=5)

button_ajouter = ttk.Button(frame_input, text="AJOUTER", command = add_task)
button_ajouter.grid(row=1, column=0, padx=5, pady=5)

task_box = tk.Listbox(frame_input, width=50, height=10)
task_box.grid(row=2, column=0, padx=5, pady=5)

button_valider = ttk.Button(frame_input, text="Valider", command = validate_task)
button_valider.grid(row=3, column=0, padx=5, pady=5)

button_supprimer = ttk.Button(frame_input, text="Supprimer", command = delete_task)
button_supprimer.grid(row=3, column=1, padx=5, pady=5)


root.mainloop()
