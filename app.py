from tkinter import *
import string
import random
from os import path
from cryptography.fernet import Fernet

# init
root = Tk()
root.title("Password Manager")
root.eval('tk::PlaceWindow . center')
root.geometry("300x420")


def create_secret_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_secret_key():
    with open("key.key", "rb") as f:
        key = f.read()
        return key


def save_to_file(site, login, password):
    with open("passwords.txt", "a+") as f:
        encrypted = Fernet(load_secret_key()).encrypt(password.encode())
        f.write(site + ":" + login + "|" + encrypted.decode() + "\n")


def read_password_file():
    # TODO:
    pass


def generate_password():
    password_input.delete(0, END)
    password = "".join([random.choice(
        string.ascii_letters + string.punctuation + string.digits) for _ in range(12)])
    password_input.insert(0, password)


def exit():
    global root
    root.quit()


# labels
website_label = Label(text="Website", pady=5)
website_label.grid(column=0, row=0, sticky=W)
login_label = Label(text="Login", pady=5)
login_label.grid(column=0, row=1, sticky=W)
password_label = Label(text="Password", pady=5)
password_label.grid(column=0, row=2, sticky=E)

# inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=0)
login_input = Entry(width=35)
login_input.grid(column=1, row=1)
login_input.insert(0, "name@email.com")
password_input = Entry(width=35)
password_input.grid(column=1, row=2)
password_input.insert(0, "************")

# buttons
read_button = Button(text="Open file", command=read_password_file)
read_button.grid(column=1, row=3, sticky="WE", pady=5)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=4, sticky="WE", pady=5)
store_to_file_button = Button(text="Store to file")
store_to_file_button.grid(column=1, row=5, sticky="WE", pady=5)
exit_button = Button(text="Exit", command=exit)
exit_button.grid(column=1, row=7, sticky="WE", pady=10)

# text area
txt_area = Text(root, width=25, height=10, pady=5)
txt_area.grid(column=1, row=6)


root.mainloop()
