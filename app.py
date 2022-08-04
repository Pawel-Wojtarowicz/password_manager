from tkinter import *

root = Tk()
root.title("Password Manager")
root.eval('tk::PlaceWindow . center')
root.geometry("300x430")


def open_txt():
    pass


# labels
website = Label(text="Website", pady=5)
website.grid(column=0, row=0, sticky="W")
email = Label(text="Email", pady=5)
email.grid(column=0, row=1, sticky="W")
password = Label(text="Password", pady=5)
password.grid(column=0, row=2)

# inputs
website.input = Entry(width=35)
website.input.grid(column=1, row=0)
email.input = Entry(width=35)
email.input.grid(column=1, row=1)
password.input = Entry(width=35)
password.input.grid(column=1, row=2)

# buttons
open = Button(text="Open file", command=open_txt)
open.grid(column=1, row=3, sticky="WE", pady=5)
generate = Button(text="Generate Password")
generate.grid(column=1, row=4, sticky="WE", pady=5)
save = Button(text="Save file")
save.grid(column=1, row=5, sticky="WE", pady=5)

# text area
txt_area = Text(root, width=25, height=10, pady=5)
txt_area.grid(column=1, row=6)

exit = Button(text="Exit", command=open_txt)
exit.grid(column=1, row=7, sticky="WE", pady=10)
# run app
root.mainloop()
