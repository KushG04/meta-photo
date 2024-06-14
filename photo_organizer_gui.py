"""
GUI for the Meta Photo application using Tkinter
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_images_date, organize_images_camera_model

def select_directory():
    path = filedialog.askdirectory()
    if path:
        directory_path.set(path)
        organize_by = organize_by_var.get()
        if organize_by == "Date":
            organize_images_date(path)
        elif organize_by == "Camera Model":
            organize_images_camera_model(path)
        else:
            messagebox.showerror("Selection Error", "please select an organization method")

def search_images(base_path, search_term):
    results = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if search_term.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def show_search_results():
    search_term = search_entry.get()
    results_listbox.delete(0, tk.END)
    if search_term:
        results = search_images(directory_path.get(), search_term)
        for result in results:
            results_listbox.insert(tk.END, result)

root = tk.Tk()
root.title("Meta Photo")

organize_by_var = tk.StringVar()
directory_path = tk.StringVar()

tk.Label(root, text="Organize by:").pack(pady=10)
tk.Radiobutton(root, text="Date Taken", variable=organize_by_var, value="Date").pack()
tk.Radiobutton(root, text="Camera Model", variable=organize_by_var, value="Camera Model").pack()

tk.Label(root, text="Directory:").pack(pady=10)
tk.Entry(root, textvariable=directory_path).pack()

select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=20)

tk.Label(root, text="Search:").pack(pady=10)
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=show_search_results)
search_button.pack(pady=10)

results_listbox = tk.Listbox(root)
results_listbox.pack(pady=20)

root.mainloop()