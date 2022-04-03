from tkinter import *

# some constants

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry

website_text_box = Entry()
website_text_box.grid(column=1, row=1, columnspan=2, sticky="EW")
website_text_box.focus()

email_text_box = Entry()
email_text_box.grid(column=1, row=2, columnspan=2, sticky="EW")
email_text_box.insert(0, "patrykkluzik99@gmail.com")

password_text_box = Entry()
password_text_box.grid(column=1, row=3, sticky="EW")


# buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()