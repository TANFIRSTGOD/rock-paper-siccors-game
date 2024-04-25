#rock paper sciccors game

import tkinter as tk

window = tk.Tk()
window.title("Rock Paper Sciccors")
window.minsize(width=250, height=250)

def handle_button_press(event):
    window.destroy()

title = tk.Label(window, text="Rock Paper Sciccors!")
title.pack()

# Start the event loop.
window.mainloop()