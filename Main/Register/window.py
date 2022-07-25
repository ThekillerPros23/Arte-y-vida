from tkinter import *


def app(window,new=None):
    window.geometry("1360x720")
    window.configure(bg = "#3ae000")
    canvas = Canvas(
        window,
        bg = "#3ae000",
        height = 720,
        width = 1360,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./Main/Register/background.png")
    background = canvas.create_image(
        680.0, 237.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"./Main/Register/img_textBox0.png")
    entry0_bg = canvas.create_image(
        882.0, 243.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 778.0, y = 218,
        width = 208.0,
        height = 48)

    entry1_img = PhotoImage(file = f"./Main/Register/img_textBox1.png")
    entry1_bg = canvas.create_image(
        588.0, 243.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 484.0, y = 218,
        width = 208.0,
        height = 48)

    entry2_img = PhotoImage(file = f"./Main/Register/img_textBox2.png")
    entry2_bg = canvas.create_image(
        731.0, 385.0,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 559.0, y = 360,
        width = 344.0,
        height = 48)

    entry3_img = PhotoImage(file = f"./Main/Register/img_textBox3.png")
    entry3_bg = canvas.create_image(
        731.0, 516.0,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry3.place(
        x = 559.0, y = 491,
        width = 344.0,
        height = 48)

    img0 = PhotoImage(file = f"./Main/Register/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b0.place(
        x = 399, y = 576,
        width = 266,
        height = 74)

    img1 = PhotoImage(file = f"./Main/Register/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command=new,
        relief = "flat")

    b1.place(
        x = 803, y = 576,
        width = 266,
        height = 74)

    window.resizable(True, True)
    window.mainloop()
