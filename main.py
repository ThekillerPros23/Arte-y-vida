from select import select
from tkinter import *
from tkcalendar import Calendar
from database.db import *
from PIL import ImageTk, Image
import time
def total_destroy():
   main = 0
def calendar():
    new = Calendar(root,selectmode = 'day', year = 2022, month=7, day = 11 )
    new.place(x = 0, y = 0)
def main():
    root.title("Arte y vida ")
    root.geometry("1366x768")
    open = Image.open("C:/Users/Derec/")
    test = ImageTk.PhotoImage(test)
    label = Label(image=test)
    label.image = test
    label.place(x = 0, y = 0)
    nombre = StringVar()
    apellido = StringVar()
    direcion = StringVar()
    name = Label(root, text='Nombre')
    name.place(x = 0, y = 0)
    apellido = Label(root, text='Apellido')
    apellido.place(x = 80, y = 0)
    direccion = Label(root, text='Direcion')
    direccion.place(x = 0, y = 240)
    entry_text = Entry(root , text ="" )
    entry_text.place(x = 0, y = 50)
    entry_text = Entry(root , text ="" )
    entry_text.place(x = 150, y = 50)
    entry_text = Entry(root , text ="" )
    entry_text.place(x = 0, y = 200) 
    tiempo = Button(root, text = 'fecha', command=lambda:calendar())
    tiempo.place( x = 0, y = 250)
    validation_button = Button(root, text = " clientes", command=lambda:connect())
    validation_button.place(x = 500, y = 50)
root = Tk()
main()  
root.mainloop()
