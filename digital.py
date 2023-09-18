import tkinter as tk
from time import strftime, localtime

def update_time():
    current_time = strftime("%H:%M:%S", localtime())
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Helvetica", 60, "bold"), fg="white", bg="black")
label.pack()

update_time()
root.mainloop()
