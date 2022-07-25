from tkinter import *
from tkinter import ttk

def delta(window, new):


    window.geometry("1360x720")
    window.configure(bg = "#88ff11")
    canvas = Canvas(
        window,
        bg = "#88ff11",
        height = 720,
        width = 1360,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = "./Main/delta/background.png")
    background = canvas.create_image(
        680.0, 74.0,
        image=background_img)

    entry0_img = PhotoImage(file ="./Main/delta/img_textBox0.png")
    entry0_bg = canvas.create_image(
        692.0, 230.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#fffefe",
        highlightthickness = 0)

    entry0.place(
        x = 202.0, y = 200,
        width = 980.0,
        height = 58)

    img0 = PhotoImage(file ="./Main/delta/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=new,
        relief = "flat")

    b0.place(
        x = 420, y = 604,
        width = 569,
        height = 74)
    tree = ttk.Treeview(window)
    tree.insert("", END, text = "hello")
    tree.place(x = 300, y= 300, width=500, height=300)
    window.resizable(False, False)
    window.mainloop()
