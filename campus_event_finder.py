import tkinter as tk
from tkinter import messagebox
import datetime

# Event list
events = []

# Function to add event
def add_event():
    title = title_entry.get()
    date = date_entry.get()
    desc = desc_entry.get("1.0", tk.END).strip()

    if title and date:
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date
            events.append((title, date, desc))
            update_event_list()
            title_entry.delete(0, tk.END)
            date_entry.delete(0, tk.END)
            desc_entry.delete("1.0", tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date", "Please use YYYY-MM-DD format")
    else:
        messagebox.showwarning("Missing Info", "Please enter both title and date.")

# Function to update the event display
def update_event_list():
    listbox.delete(0, tk.END)
    for i, event in enumerate(events, 1):
        listbox.insert(tk.END, f"{i}. {event[0]} on {event[1]} - {event[2]}")

# Function to save to a file
def save_events():
    with open("events.txt", "w") as f:
        for event in events:
            f.write(f"{event[0]}|{event[1]}|{event[2]}\n")
    messagebox.showinfo("Saved", "Events saved to 'events.txt'.")

# GUI Setup
root = tk.Tk()
root.title("Campus Event Finder")
root.geometry("500x500")

# Input Fields
tk.Label(root, text="Event Title").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Event Date (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root, width=50)
date_entry.pack()

tk.Label(root, text="Event Description").pack()
desc_entry = tk.Text(root, height=3, width=50)
desc_entry.pack()

tk.Button(root, text="Add Event", command=add_event).pack(pady=5)
tk.Button(root, text="Save Events", command=save_events).pack(pady=5)

tk.Label(root, text="Upcoming Events").pack()
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack()

root.mainloop()
