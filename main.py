from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice


# some constants

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = [choice(letters) for _ in range(randint(8, 10))]
    numbers = [choice(numbers) for _ in range(randint(2, 4))]
    symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password = letters + numbers + symbols
    shuffle(password)

    password_entry.insert(0, ''.join(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # get data to be filled into the file

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = [
        website,
        email,
        password
    ]

    data_name = [
        "website",
        "email/username",
        "password"
    ]

    index = 0
    fields_filled = 0

    # loop through the fields and display info message for the empty field
    # if field isn't empty, then increment field filled by 1
    for field in data:
        if field == '':
            messagebox.showinfo(title="Oops", message=f"The {data_name[index]} field is empty")
        else:
            fields_filled += 1
        index += 1

    # bool to see if all entries are filled
    validated_entries = fields_filled == 3

    if validated_entries:

        # confirm with user entered details
        is_ok = messagebox.askokcancel(title=website, message=f"Confirm your detail: \n"
                                                              f"Email: {email}\n"
                                                              f"Password: {password}")

        # create a string delimited by the pipe symbol
        line_to_append = ' | '.join(data)

        if is_ok:
            # open the file and append the new line, create a new line
            with open("password_data.txt", "a") as password_file:
                password_file.write(line_to_append + "\n")

            # call delete method to clear the entry box
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- TAKE EMAIL ------------------------------- #

def get_most_recent_email_address():
    # try to open the password_data.txt file
    try:
        with open("password_data.txt") as password_file:
            # get the last line
            for line in password_file:
                pass
            # create a list for the last line
            last_line = line.split(" | ")
            # return the 1st index (email/username entry)
            return last_line[1]
    # if unable to, return empty string
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
generate_password_button.config(command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35)
add_button.config(command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
