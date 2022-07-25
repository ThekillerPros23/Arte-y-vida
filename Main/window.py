from tkinter import *
from Register.window import *
from delta.window import *
window = Tk()
def main():
   
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

    background_img = PhotoImage(file = "./Main/background.png")
    background = canvas.create_image(
        680.0, 146.5,
        image=background_img)

    img0 = PhotoImage(file = "./Main/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b0.place(
        x = 549, y = 311,
        width = 266,
        height = 74)

    img1 = PhotoImage(file = "./Main/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:app(window, lambda:main()),
        relief = "flat")
    b1["state"] = "normal"
    b1.place(
        x = 547, y = 453,
        width = 266,
        height = 74)

    img2 = PhotoImage(file = "./Main/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:delta(window, lambda:main()),
        relief = "flat")

    b2.place(
        x = 547, y = 595,
        width = 266,
        height = 74)
    window.resizable(True, True)
    window.mainloop()

main()
