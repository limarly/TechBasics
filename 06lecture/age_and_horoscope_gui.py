import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

# create the gui window
root = tk.Tk()

# title
root.title('Age Calculator')

# configure the size
screen_height = 400
screen_width = 600
root.minsize(width=screen_width, height=screen_height)


# place an image on the first screen
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


add_image(root, "images/age_calculator.png", screen_width, screen_height)


def calculate_age():
    # get today's date
    current_date = date.today()

    # get the users dob
    dob = cal.get_date()

    # if the year of dob is greater than existing year, subtract 100
    if dob.year > current_date.year:
        dob = dob - relativedelta(years=100)

    age = int((current_date - dob).days / 365.25)

    age_label = tk.Label(root,
                         text=f"You age is {age}",
                         bg="white",
                         fg="black"
                         )
    age_label.place(x=screen_width/2-70, y=200)


# launch an image on the first screen

def calculate_age_page():
    global cal

    # destroy everything we've created so far
    f1.destroy()
    entry_button.destroy()

    # change background colour
    root.configure(background="white")

    # creating a label to ask user for their dob
    dob_label = tk.Label(root,
                         text="Enter your Date of Birth",
                         font="impact 32 bold",
                         fg="blue",
                         bg="white"
                         )
    dob_label.pack(anchor="center")

    # creating a calendar entry point
    cal = DateEntry(root,
                    font="Arial 20",
                    selectmode="day")
    cal.pack(anchor="center")

    # button to calculate the age
    calc_age_button = tk.Button(root,
                                text="Calculate the age",
                                font="Arial 16 bold",
                                command=calculate_age
                                )
    calc_age_button.pack(anchor="center", padx=10, pady=10)


# create an entry button which will enter the next page
entry_button = tk.Button(root,
                         text="Click here to start",
                         bg="blue",
                         font="Arial 20 bold",
                         command=calculate_age_page)
entry_button.pack(anchor="center")

root.mainloop()
