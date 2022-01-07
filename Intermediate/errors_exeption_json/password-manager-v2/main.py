import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find Password --------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

# Website entry
website_entry = Entry(width=25)
website_entry.focus()
website_entry.grid(column=1, row=1)

# Search Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

# Email/Username label
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

# User entry
user_entry = Entry(width=42)
user_entry.insert(0, "helloworld@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

# Password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Password entry
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Generate password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", command=save_info, width=41)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
