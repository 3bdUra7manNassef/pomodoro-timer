from tkinter import Tk, Label, Button
import os
os.system("pip install customtkinter")
os.system("pip install pywinstyles")
import pywinstyles
import customtkinter as ctk
def start_timer(minutes, seconds):
    if minutes == 0 and seconds == 0:
        return
    time_string = f"{minutes:02d}:{seconds:02d}"
    label.configure(text=time_string)

    if seconds == 0:
        minutes -= 1
        seconds = 59
    elif seconds == 1 and minutes ==  0:
        Label(root,text='the timer is ending')
    else:
        seconds -= 1

    root.after(1000, start_timer, minutes, seconds)

def start_pomodoro():
    start_timer(25, 0)

root = ctk.CTk()
root.title("Pomodoro Timer")
root.geometry("300x200")  # Set the size of the window
root.iconbitmap('pomodoro ico.ico')
root.resizable(False,False)
pywinstyles.apply_style(root, 'aero')

label = ctk.CTkLabel(root,bg_color='transparent', text="25:00",width=100,height=70,font=('Arial',35,'bold'))
label.pack()

start_button = ctk.CTkButton(root,fg_color='#229954',hover_color='#196F3D',width=140,height=60,corner_radius=15,text="Start",font=('Constantia',26,'bold'), command=start_pomodoro)
start_button.place(x=80,y=100)
ctk.CTkButton(root)
root.mainloop()
