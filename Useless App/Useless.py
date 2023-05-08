import tkinter as tk
import random
from time import sleep

def type_writer_effect(label, text, delay=0.1):
    for i, char in enumerate(text):
        label.config(text=label.cget("text") + char)
        label.update()
        sleep(delay)

def hello_world_effect():
    label4.config(text="")
    label4.update()
    sleep(1)
    type_writer_effect(label4, "Hello World!", 0.2)

def simulate_hacking():
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")

    label2.update()
    label3.update()
    label4.update()

    sleep(0.5)

    type_writer_effect(label2, "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(25)]), 0.05)
    type_writer_effect(label3, "".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(25)]), 0.05)

    hello_world_effect()

window = tk.Tk()

window.title("Hacking into your system...")
window.geometry("400x200")
window.configure(bg="black")

label = tk.Label(window, text="Hacking into your system...", font=("Arial Bold", 20), fg="green", bg="black")
label.grid(column=0, row=0)

label2 = tk.Label(window, text="...", font=("Arial Bold", 20), fg="green", bg="black")
label2.grid(column=0, row=1)

label3 = tk.Label(window, text="...", font=("Arial Bold", 20), fg="green", bg="black")
label3.grid(column=0, row=2)

label4 = tk.Label(window, text="...", font=("Arial Bold", 20), fg="green", bg="black")
label4.grid(column=0, row=3)

button = tk.Button(window, text="Click Me", command=simulate_hacking)
button.grid(column=0, row=4)

window.mainloop()
