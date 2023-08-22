# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:57:10 2023

@author: Pakhomav
"""

import tkinter as tk
from tkinter import font
import random

def get_complementary_color(color):
    r, g, b = color
    complementary_r = 255 - r
    complementary_g = 255 - g
    complementary_b = 255 - b
    return (complementary_r, complementary_g, complementary_b)

def update_bg_color():
    color_code = b.get()
    try:
        color_code = "#" + color_code.strip("#")
        color_tuple = tuple(int(color_code[i:i+2], 16) for i in (1, 3, 5))
        complementary_color = get_complementary_color(color_tuple)
        root.configure(background=color_code)
        color_entry.config(bg=color_code)
        label.config(bg=color_code, fg="#%02x%02x%02x" % complementary_color)
        a.set(color_code)
    except ValueError:
        pass

def generate_random_color():
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    b.set(random_color)
    update_bg_color()

def clear():
    b.set('')
    color_entry.delete(0, 'end')

root = tk.Tk()
root.title('Chamaeleonidae_colorchart')
width = 900
height = 700
left = 0
top = 0
root.configure(background='#000000')
root.geometry(f'{width}x{height}+{left}+{top}')

a = tk.StringVar()
b = tk.StringVar()
a.set('#000000')

color_entry = tk.Entry(root, textvariable=b)
color_entry.pack(padx=20, pady=20)

update_button = tk.Button(root, text="CHANGE COLOR", command = update_bg_color)
update_button.pack()

update_button2 = tk.Button(root, text="RANDOM COLOR", command = generate_random_color)
update_button2.pack()

available_fonts = font.families()
selected_font = "Cascadia Mono"
label_font = font.Font(family=selected_font, size=100)
label = tk.Label(root, textvariable=a,
                 font=label_font,
                 pady=10,
                 borderwidth=20,
                 wraplength=700,
                 fg = "#ffffff"
                 )
label.pack(fill='both', expand=True)
label.configure(bg=root.cget('bg'))

after_id = None
root.mainloop()





