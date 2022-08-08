from tkinter import *
import string
import random

root = Tk()
root.title("Password Manager")
root.eval('tk::PlaceWindow . center')
root.geometry("300x420")


def open_txt():
    pass


def exit():
    global root
    root.quit()


def generate_password():
    password_input.delete(0, END)
    password = "".join([random.choice(
        string.ascii_letters + string.punctuation + string.digits) for _ in range(8)])
    password_input.insert(0, password)


# labels
website_label = Label(text="Website", pady=5)
website_label.grid(column=0, row=0, sticky=W)
email_label = Label(text="Email", pady=5)
email_label.grid(column=0, row=1, sticky=W)
password_label = Label(text="Password", pady=5)
password_label.grid(column=0, row=2, sticky=E)

# inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=0)
email_input = Entry(width=35)
email_input.grid(column=1, row=1)
email_input.insert(0, "name@email.com")
password_input = Entry(width=35)
password_input.grid(column=1, row=2)
password_input.insert(0, "********")

# buttons
open_button = Button(text="Open file", command=open_txt)
open_button.grid(column=1, row=3, sticky="WE", pady=5)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=4, sticky="WE", pady=5)
save_button = Button(text="Save file")
save_button.grid(column=1, row=5, sticky="WE", pady=5)

# text area
txt_area = Text(root, width=25, height=10, pady=5)
txt_area.grid(column=1, row=6)


exit_button = Button(text="Exit", command=exit)
exit_button.grid(column=1, row=7, sticky="WE", pady=10)
# run app
root.mainloop()
