import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()

root.title("Hangman")

root.minsize(width=450, height=450)

root.configure(background="white")

def display_secret_word(word_list):

    #select a random word
    secret_word = (random.choice(word_list))

    #display the dashes - we are storing this as a list so wen can manipulate it later on
    display_word = list("_"*len(secret_word))

    return secret_word, display_word

word_list = ["dog", "sweet", "zebra", "cat"]
secret_word, display_word = display_secret_word(word_list)

title = tk.Label(root,
                 text = "Guess the letter",
                 font="Geneva 25",
                 bg="white",
                 fg="black")
title.place(x=110, y=0)

guessed_letter = tk.StringVar()
letter_entry = tk.Entry(root,
                        bg="white",
                        fg="black",
                        textvariable=guessed_letter)
letter_entry.place(x=100, y=350)

display = tk.Label(root,
                   text=display_word,
                   font="Geneva 20",
                   bg="white",
                   fg="black")
display.place(x=140, y=55)

def play_hangman():
    global guessed_letter, secret_word, display, display_word

    # if user guesses the secret word correctly
    if guessed_letter.get() in secret_word:
        # replace the dashes with the guessed letter
        for i in range(len(secret_word)):
            if list(secret_word)[i] == guessed_letter.get():
                display_word[i] = guessed_letter.get()

        #update your display label with the correct letter
        display.configure(text=display_word)


        if "".join(display_word) == secret_word:
            #update the box where user enters the letter
            title.configure(text="YOU WON")
            #destroy the box where user enters the letter
            letter_entry.destroy()
            #update the play button
            play_button.configure(text="PLAY AGAIN?!")



play_button = tk.Button(root,
                   text="LET'S PLAY",
                   command=play_hangman)
play_button.place(x=150, y=400)

root.mainloop()