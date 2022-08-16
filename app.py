from tkinter import *
import string
import random
from os import path
from tkinter import messagebox
from cryptography.fernet import Fernet


# init
root = Tk()
root.title("Password Manager")
root.eval('tk::PlaceWindow . center')
root.geometry("400x420")


def create_secret_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


def load_secret_key():
    with open("key.key", "rb") as f:
        key = f.read()
        return key


def save_to_file():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    if len(website) == 0 or len(login) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error!", message="Don't leave any empty boxes!")
    else:
        with open("passwords.txt", "a+") as f:
            encrypted = Fernet(load_secret_key()).encrypt(password.encode())
            f.write(website + ":" + login + ":" + encrypted.decode() + "\n")


def load_password_file():
    txt_area.delete("1.0", END)
    passwords = []
    with open("passwords.txt", "r") as f:
        for line in f:
            site, login, encrypted = line.split(":")
            decrypted = Fernet(load_secret_key()).decrypt(encrypted.encode())
            password = decrypted.decode('utf-8')
            passwords.append(site + ": " + login + ": " + password)
    for password in passwords:
        txt_area.insert(END, password + "\n")


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
website_input = Entry(width=55)
website_input.grid(column=1, row=0)
login_input = Entry(width=55)
login_input.grid(column=1, row=1)
login_input.insert(0, "name@email.com")
password_input = Entry(width=55)
password_input.grid(column=1, row=2)
#password_input.insert(0, "************")

# buttons
read_button = Button(text="Open file", command=load_password_file)
read_button.grid(column=1, row=3, sticky="WE", pady=5)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=1, row=4, sticky="WE", pady=5)
store_to_file_button = Button(text="Store to file", command=save_to_file)
store_to_file_button.grid(column=1, row=5, sticky="WE", pady=5)
exit_button = Button(text="Exit", command=exit)
exit_button.grid(column=1, row=7, sticky="WE", pady=10)

# text area
txt_area = Text(root, width=40, height=10, pady=5)
txt_area.grid(column=1, row=6)


root.mainloop()
