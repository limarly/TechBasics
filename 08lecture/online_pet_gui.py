import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import pandas as pd
from tkinter import messagebox

root = tk.Tk()

root.title('My Online Pet')

screen_width = 650
screen_height = 400
root.minsize(width=screen_width, height=screen_height)


def add_image(root, file_path, width, height):
    global pic, f1
    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image you want to use for the first fra,e
    img = Image.open(file_path)
    # resize the image
    img = img.resize((width, height), Image.LANCZOS)
    # add this code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    lab = tk.Label(f1, image=pic)
    lab.pack()
    f1.pack()


def enter_user_data():
    # gives me the current timestamp
    current_timestamp = datetime.now()

    # create a dictionary that stores the information the user enters and a timestamp field
    user_data = {
        "name_of_user": name.get(),
        "user_id": username.get(),
        "favourite_pet": favourpet.get(),
        "created_at": current_timestamp
    }
    # reads the user ids in the csv file
    user_ids = list(pd.read_csv("data/user_data.csv").user_id)

    # if the username already exists then print a warning box
    if username.get() in user_ids:
        tk.messagebox.showwarning("Warning!", "This username already exists")
    # otherwise write the data to the csv file
    else:
        # converts the dictionary into a data frame
        user_data_df = pd.DataFrame([user_data])
        # write to a csv file
        user_data_df.to_csv("data/user_data.csv", index=False, mode='a', header=False)

        # clear all the widgets that were created
        for i in root.winfo_children():
            i.destroy()

        # add a thank you label
        thankyou_label = tk.Label(root,
                                  text=f"Welcome to Online Pets {name.get()}!",
                                  font=("Comic Sans MS", 20, "bold"))
        thankyou_label.pack(side=tk.TOP)


def clear_widgets():
    for i in root.winfo_children():
        i.destroy()


def create_new_user_page():
    global homepage, username, name, new_label, name_label, username_label, name_box, username_box, favourpet, favepet_label, favepet_box
    # destroy everything we created in our homepage
    f1.destroy()
    welcome_label.destroy()
    new_user.destroy()
    returning_user.destroy()

    # create a button for the users to go back to the home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage)
    homepage.pack(side=tk.BOTTOM)

    # create lable and entry boxes
    new_label = tk.Label(root,
                         text="WELCOME NEW USER!",
                         font=("Comic Sans MS", 20, "bold"))
    new_label.pack(side=tk.TOP, anchor=tk.CENTER)

    # get some information about the user
    name_label = tk.Label(root,
                          text="What is your name?")
    name_label.place(x=50, y=100)

    # entry box
    name = tk.StringVar()
    name_box = tk.Entry(root,
                        textvar=name,
                        fg="black",
                        bg="white")
    name_box.place(x=250, y=100)

    # get some information about the user
    username_label = tk.Label(root,
                              text="Create a username")
    username_label.place(x=50, y=150)

    # entry box
    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvar=username,
                            fg="black",
                            bg="white")
    username_box.place(x=250, y=150)

    # get some information about the user
    favepet_label = tk.Label(root,
                             text="What is your favourite pet?")
    favepet_label.place(x=50, y=200)

    # entry box
    favourpet = tk.StringVar()
    favepet_box = tk.Entry(root,
                           textvar=favourpet,
                           fg="black",
                           bg="white")
    favepet_box.place(x=250, y=200)

    #
    enter_data = tk.Button(root,
                           text="Submit Info",
                           font=("Comic Sans MS", 15, "bold"),
                           command=enter_user_data)
    enter_data.pack(side=tk.BOTTOM)


def create_returning_user_page():
    global homepage

    # destroy everything we created in our homepage
    f1.destroy()
    welcome_label.destroy()
    new_user.destroy()
    returning_user.destroy()

    # create a button for the users to go back to the home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=create_homepage)
    homepage.pack(side=tk.BOTTOM)


def create_homepage():
    global welcome_label, new_user, returning_user

    # For cleanliness, you can write the try except command for every page like here
    """try:  # try to destroy homepage if it is there
        homepage.destroy()
    except:  # otherwise just pass
        pass"""

    """try:  # try to destroy homepage if it is there
        homepage.destroy()  # destroy from homepage (first page)
        new_label.destroy()  # from here till favepet_box destroy from second page
        name_label.destroy()
        username_label.destroy()
        name_box.destroy()
        username_box.destroy()
        favepet_label.destroy()
        favepet_box.destroy()
    except:  # otherwise just pass
        pass"""

    # destroys everywidget that has been created so far
    for i in root.winfo_children():
        # if i.winfo_name() != ".!button3":
        # root.winfo_children is a list, so if you would like to exclude certain widgets
        # exclude them from the list
        # print(i)
        i.destroy()

    # add a background to your first page
    add_image(root, "images/cat_image.jpg", screen_width, screen_height)

    welcome_label = tk.Label(root,
                             text="Welcome to my Online Pets Page",
                             font=("Comic Sans MS", 30, "bold"),
                             fg="black",
                             bg="white")
    welcome_label.place(x=60, y=60)

    # create a new user button
    new_user = tk.Button(root,
                         text="New User",
                         font=("Comic Sans MS", 15),
                         command=create_new_user_page)

    # create a returning user button
    returning_user = tk.Button(root,
                               text="Returning User",
                               font=("Comic Sans MS", 15),
                               command=create_returning_user_page)

    new_user.pack()
    returning_user.pack()


# create the home page
create_homepage()

root.mainloop()
