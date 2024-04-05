from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json


def generate_number():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


def search():
    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="the file Not found")
    else:
        website = website_entry.get()
        if website in data:
            password = data[website]["password"]
            user = data[website]["user"]
            messagebox.showinfo(title=website, message=f"mail:{user}\npassword:{password}")
        else:
            messagebox.showerror(message="the website not found")


def write():
    is_ok = False
    user = user_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    dic = {
        website: {
            "user": user,
            "password": password
        }
    }
    if len(password) == 0 or len(user) == 0 or len(website) == 0:
        messagebox.showwarning(title="Warning", message="You should not leave any filed empty")
    else:
        is_ok = messagebox.askokcancel(title="check info", message="press Ok if your info is right")
    if is_ok:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
                data.update(dic)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(dic, file, indent=4)
        else:
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            user_entry.delete(0, END)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


window = Tk()
window.title("password Manger")
window.config(pady=50, padx=50)
photo = PhotoImage(file="logo.png")
canvas = Canvas(width=140, height=180)
canvas.create_image(80, 80, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/User")
user_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)
user_entry = Entry(width=39)
user_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

search_button = Button()
search_button.config(text="search password", width=14, command=search)
search_button.grid(column=2, row=1, sticky="W")
generate_button = Button()
generate_button.config(text="Generate password", width=14, command=generate_number)
generate_button.grid(column=2, row=3, sticky="W")
add_button = Button()
add_button.config(text="Add", width=36, command=write)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
