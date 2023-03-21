import tkinter
from tkinter import messagebox
import time
import winsound
from tkinter import simpledialog

# This deals with the main interface of the app.
interface = tkinter.Tk()
interface.configure(background='Black')
interface.title('Timer')
interface.geometry('600x450')

icon = tkinter.PhotoImage(file='tomato.png')
interface.iconphoto(True, icon)

# this defines the app and runs the clock
def the_clock():
    """Sets the clock to 24 hour time"""
    hour = time.strftime('%H')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    day = time.strftime('%D')

    label.config(text=f'{hour}:{minutes}:{seconds}')
    label.after(1000, the_clock)

    label2.config(text=f'{day}')


label = tkinter.Label(interface, text='', font=('SF Pro Display', 72), foreground='White', background='Black')
label.pack(pady=30)
label2 = tkinter.Label(interface, text='', font=('SF Pro Display', 20), foreground='White', background='Black')
label2.pack(pady=0)


# this runs the pomodoro function of the app.
def start_pomodoro():
    """Starts the pomodoro time to 50/10 intervals"""
    work_time = simpledialog.askinteger("Work Time", "Enter the work time in minutes:", minvalue=1)
    break_time = simpledialog.askinteger("Break Time", "Enter the break time in minutes:", minvalue=1)

    work_time_seconds = work_time * 60
    break_time_seconds = break_time * 60

    # Flag to stop the loop
    stop_flag = False

    # Stop button event handler
    def stop_pomodoro():
        nonlocal stop_flag
        stop_flag = True
        pomodoro_label.config(text='00:00')
        interface.update()

    # Create and pack the stop button
    stop_button = tkinter.Button(interface, text='Stop', font=('SF Pro Display', 10, 'bold'), background='Black', foreground='White', command=stop_pomodoro)
    stop_button.pack(padx=10, pady=10)

    cont = True
    while cont == True and not stop_flag:
        for i in range(work_time_seconds, -1, -1):
            minute = i // 60
            seconds = i % 60
            pomodoro_label.config(text=f'{str(minute).zfill(2)}:{str(seconds).zfill(2)}')
            interface.update()
            time.sleep(1)
            if stop_flag: break

        if stop_flag: break

        for i in range(5):
            winsound.Beep(i + 100, 500)

        messagebox.showinfo("Break time", f'{break_time} minute break')

        if stop_flag: break

        for i in range(break_time_seconds, -1, -1):
            minute = i // 60
            seconds = i % 60
            pomodoro_label.config(text=f'{minute}:{seconds}')
            interface.update()
            time.sleep(1)
            if stop_flag: break

        if stop_flag: break

        continuation = messagebox.askyesno('Do you want to continue?')
        if continuation == True:
            continue
        else:
            break

    # Remove the stop button
    stop_button.pack_forget()

pomodoro_button = tkinter.Button(interface, text='Start Pomodoro', font=('SF Pro Display', 10, 'bold'), background='Black', foreground='White', command=start_pomodoro)
pomodoro_button.pack(padx=10, pady=10)
pomodoro_label = tkinter.Label(interface, text='', font=('SF Pro Display', 72), foreground='White', background='Black')
pomodoro_label.pack(padx=10, pady=10)

the_clock()
interface.mainloop()
