import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        contact_listbox.insert(tk.END, f"{name} - {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Both name and phone number are required.")

def delete_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contact_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact to delete.")

def view_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contact = contact_listbox.get(selected_index)
        messagebox.showinfo("Contact Info", contact)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a contact to view.")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create widgets for adding contacts
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=1, column=0, padx=10, pady=10)

phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create the listbox to display contacts
contact_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE, borderwidth=5, relief=tk.SUNKEN)
contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create buttons for deleting and viewing contacts
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, pady=10)

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.grid(row=4, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
