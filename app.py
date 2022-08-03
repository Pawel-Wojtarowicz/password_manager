from tkinter import *


root = Tk()
root.title("Password Manager")
root.eval('tk::PlaceWindow . center')
logo = PhotoImage(file=r"D:\Python_repositories\password_manager\logo1.png")
canvas = Canvas(width=300,height=300)
canvas.configure(background="blue")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0)


title = Label(text="Password Manager", font=("TkMenuFont", 16))
title.grid(column=0, row=1)

title1 = Label(text="test", font=("TkMenuFont", 16))
title1.grid(column=0, row=2)


#run app
root.mainloop()