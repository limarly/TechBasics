import tkinter as tk
from PIL import Image, ImageTk
import random

# code to create the gui window
root = tk.Tk()

# give your gui a title
root.title("Hangman")

# code to configure the size
root.geometry("650x450")

# Create the frame for the first windows of the game
f1 = tk.Frame(root)
# read the image you want to use for the first fra,e

f1.pack()

word_list = ["dog", "sweet", "zebra", "cat"]

def display_secret_word(word_list):

    #select a random word
    secret_word = (random.choice(word_list))

    #display the dashes - we are storing this as a list so wen can manipulate it later on
    display_word = list("_"*len(secret_word))

    return secret_word, display_word

final = display_secret_word(word_list)
print(final)