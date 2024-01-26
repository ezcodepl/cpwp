# python Copy Windows profile
import os
from tkinter import *

ws = Tk()
ws.title('Windows 10 / Windows 11 copy User Profile')
w = 1820  # Width
h = 1080  # Height

screen_width = ws.winfo_screenwidth()  # Width of the screen
screen_height = ws.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)

ws.geometry('%dx%d+%d+%d' % (w, h, x, y))
ws.minsize(800, 600)
ws['bg'] = '#76a5af'

#bg = '#76a5af', #45818e #134f5c
#source computer
src_txt = Label(
    ws,
    text="Wpisz adres komputera źródłowego:",
    bg='#76a5af',
    fg='#fff',
    font=("Verdana 10")
)
src_txt.place(x=20, y=40)

src_input = Entry(ws, width='45')
src_input.place(x=340, y=40)

src_usr = Label(
    ws,
    text="Wpisz nazwę użytkownika:",
    bg='#76a5af',
    fg='#fff',
    font=("Verdana 10")
)
src_usr.place(x=20, y=80)
src_usr_input = Entry(ws, width='25')
src_usr_input.place(x=260, y=80)

#destination computer
dsc_txt = Label(
    ws,
    text="Wpisz adres komputera docelowego:",
    bg='#76a5af',
    fg='#fff',
    font=("Verdana 10")
)
dsc_txt.place(x=1100, y=40)

dsc_input = Entry(ws, width='45')
dsc_input.place(x=1425, y=40)

dsc_usr = Label(
    ws,
    text="Wpisz nazwę użytkownika:",
    bg='#76a5af',
    fg='#fff',
    font=("Verdana 10")
)
dsc_usr.place(x=1100, y=80)
dsc_usr_input = Entry(ws, width='25')
dsc_usr_input.place(x=1340, y=80)

# # appends current content of l_one with the new pressed key value
# def callback(event):
#     l_one.config(text=src_input.get() + event.char)
#
# # binds callback to every keypress
# src_input.bind("<Key>", callback)
#
# l_one = Label(ws, bg='#76a5af', fg='#fff', font=("Verdana 10"))
# l_one.place(x=20, y=120)
def display_folder_contents(folder_path):
    try:
        folder_contents = os.listdir(folder_path)
        ws.Listbox.delete(0, ws.END)  # Clear the current list

        for item in folder_contents:
            ws.Listbox.insert(ws.END, item)

    except Exception as e:
        ws.Listbox.delete(0, ws.END)  # Clear the current list
        ws.Listbox.insert(ws.END, f"Error: {str(e)}")

folder_list = Listbox(ws)
folder_list.pack()

ws.mainloop()