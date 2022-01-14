import tkinter as tk
from tkinter import messagebox
import random
import pyperclip as pc

# ---------------------------- UI SETUP ------------------------------- #


# Create the window
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

# Canvas
canvas = tk.Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_image = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# website label
website_label = tk.Label()
website_label.config(text='Website:', bg='white')
website_label.grid(column=0, row=1)

# email label
email_label = tk.Label()
email_label.config(text='Email/Username:', bg='white')
email_label.grid(column=0, row=2)

# password label
pw_label = tk.Label()
pw_label.config(text='Password:', bg='white')
pw_label.grid(column=0, row=3)

# website input
website_entry = tk.Entry(width=50)
website_entry.grid(column=1, columnspan=2, row=1)

# email input
email_entry = tk.Entry(width=50)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0, 'test@gmail.com')

# password input
pw_entry = tk.Entry(width=32)
pw_entry.grid(column=1, row=3)


def add_new_entry():
    new_website_entry = website_entry.get()
    new_email_entry = email_entry.get()
    new_pw_entry = pw_entry.get()

    # validate if any of the entries are blank
    if len(new_website_entry) == 0 or len(new_email_entry) == 0 or len(new_pw_entry) == 0:
        messagebox.showwarning(title='Warning', message='Missing key info, please check again.')
    else:
        # create message box to ask user to validate entry
        is_ok = messagebox.askokcancel(title=new_website_entry,
                                       message='Is it ok to save the following information?'
                                               '\nEmail: {}\nPassword: {}'.format(new_email_entry, new_pw_entry))
        # proceed to write to files
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write('\n{}|{}|{}'.format(new_website_entry, new_email_entry, new_pw_entry))
                website_entry.delete(0, tk.END)
                pw_entry.delete(0, tk.END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_random_pw():
    password_list = []

    password_list.extend([random.choice(letters) for _ in range(random.randint(8, 10))])
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])
    random.shuffle(password_list)
    random_pw = ''.join(password_list)
    pw_entry.insert(0, random_pw)
    pc.copy(random_pw)  # directly copy to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def click_generate_pw():
    generate_random_pw()


# generate password button
pw_generate_button = tk.Button(text='Generate Password', command=click_generate_pw)
pw_generate_button.grid(column=2, row=3)

# Add button
add_button = tk.Button(text='Add', width=43, command=add_new_entry)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
