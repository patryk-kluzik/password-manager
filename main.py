from tkinter import *


# some constants

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # get data to be filled into the file

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = [website, email, password]

    line_to_append = ' | '.join(data)

    with open("password_data.txt", "a") as password_file:
        password_file.write(line_to_append + "\n")


# ---------------------------- TAKE EMAIL ------------------------------- #

def get_most_recent_email_address():
    try:
        with open("password_data.txt") as password_file:
            for line in password_file:
                pass
            last_line = line.split(" | ")
            return last_line[1]
    except:
        return ""


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

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, get_most_recent_email_address())

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35)
add_button.config(command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
