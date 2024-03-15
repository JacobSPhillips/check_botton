from tkinter import *


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

x = IntVar()

check_button = Checkbutton(
    window,
    text='I agree to something',
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    fg='#00ff00',
    bg='black',
    activeforeground='#00ff00',
    activebackground='black',
    padx=25,
    pady=25
)
check_button.pack()

window.mainloop()
