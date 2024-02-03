# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:05:20 2024

@author: Aidan
"""

from tkinter import*
from tkinter import ttk

root = Tk()
root.title("P166-167")
root.geometry("1000x600")

canvas = Canvas(root, width=990, height=490, bg="white", highlightbackground="cyan")
canvas.pack()
colores = ["Lime", "cyan", "black", "red"]
color_dropdown = ttk.Combobox(root, state="readonly", values = colores, width=10)
color_dropdown.place(relx=0.8, rely=0.9, anchor=CENTER)

start_x = Label(root, text="inicio x: ")
start_x.place(relx=0.1, rely=0.85, anchor=CENTER)

coordenadas = [10,50,100,200,300,400,500,600,700,800,900]
coord_dropdown = ttk.Combobox(root, state="readonly", values = coordenadas, width=10)
coord_dropdown.place(relx=0.2, rely=0.85, anchor=CENTER)

starty = Label(root, text="inicio y: ")
starty.place(relx=0.1, rely=0.85, anchor=CENTER)

coordy_dropdown = ttk.Combobox(root, state="readonly", values = coordenadas, width=10)
coordy_dropdown.place(relx=0.4, rely=0.85, anchor=CENTER)

endx = Label(root, text="final x: ")
endx.place(relx=0.5, rely=0.85, anchor=CENTER)

coordfx_dropdown = ttk.Combobox(root, state="onlyread", values = coordenadas, width = 10)
coordfx_dropdown.place(relx=0.6, rely=0.85, anchor=CENTER)

endy = Label(root, text="final y : ")
endy.place(relx=0.7, rely=0.85, anchor=CENTER)

coordify_dropdown = ttk.Combobox(root, state="onlyread", values = coordenadas, width = 10)
coordify_dropdown.place(relx=0.8, rely=0.85)

def circle(event):
    oldx = coord_dropdown.get()
    oldy = coordy_dropdown.get()
    neyx = coordfx_dropdown.get()
    newy = coordfy_dropdown.get()
    keypress = "c"
    draw(keypress, oldx, oldy, newx, newy)
    
def rectangle(event):
    oldx = coord_dropdown.get()
    oldy = coordy_dropdown.get()
    neyx = coordfx_dropdown.get()
    newy = coordfy_dropdown.get()
    keypress = "r"
    draw(keypress, oldx, oldy, newx, newy)
    
def line(event):
    oldx = coord_dropdown.get()
    oldy = coordy_dropdown.get()
    neyx = coordfx_dropdown.get()
    newy = coordfy_dropdown.get()
    keypress = "l"
    draw(keypress, oldx, oldy, newx, newy)
    
def draw(keypress, oldx, oldy, newx, newy):
    color = color_dropdown.get()
    if keypress== "c":
        draw_circle = canvas.create_oval(oldx, oldy, newx, newy, fill=color)
    if keypress== "r":
        draw_rectangle = canvas.create_rectangle(oldx, oldy, newx, newy, fill=color)
    if keypress== "l":
        draw_line = canvas.create_line(oldx, oldy, newx, newy, fill=color)

root.bind("<c>", circle)
root.bind("<r>", rectangle)
root.bind("<l>", line)

root.mainloop()



