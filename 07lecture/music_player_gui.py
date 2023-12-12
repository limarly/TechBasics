import os
import tkinter as tk
from tkinter.filedialog import askdirectory
import pygame as pg

# crate th egui window
root = tk.Tk()

# title
root.title('Music Gui')

# configure the size
screen_height = 350
screen_width = 450
root.minsize(width=screen_width, height=screen_height)

# create the directory box
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()  # this gives all the song in the folder you selected

# create a list box, that will contain all the songs in the folder I select
play_list = tk.Listbox(root,
                       font="Arial 12 bold",
                       bg="yellow",
                       fg="black",
                       selectmode=tk.SINGLE)  # select one item at a time

# place the song name in the list box
pos = 0
for song in song_list:
    play_list.insert(pos, song)
    pos += 1

# initialise the pygame library
pg.init()


def play_music():
    pg.mixer.music.load(play_list.get(tk.ACTIVE))  # loads thw file that you select in your listbox
    song_name.set(play_list.get(tk.ACTIVE))

    pg.mixer.music.play()


def play_music_selection(event):
    play_music()
    # TODO: this is how you write a todo note
    # will reset the pause button if necessary
    pause_button.configure(text="PAUSE",
                           command=pause_music)


def stop_music():
    pg.mixer.music.stop()
    pause_button.configure(text="PAUSE",
                           command=pause_music)


def pause_music():
    pg.mixer.music.pause()
    pause_button.configure(text="UNPAUSE", command=unpause_music)


def unpause_music():
    pg.mixer.music.unpause()
    pause_button.configure(text="PAUSE",
                           command=pause_music)


# CREATE BUTTONS
# play
play_button = tk.Button(root,
                        text="Play",
                        height=3,
                        font="Arial 12 bold",
                        highlightbackground="blue",
                        highlightthickness="10",
                        fg="black",
                        command=play_music)

# stop
stop_button = tk.Button(root,
                        text="STOP",
                        height=3,
                        font="Arial 12 bold",
                        highlightbackground="red",
                        highlightthickness="10",
                        fg="black",
                        command=stop_music)
# pause
pause_button = tk.Button(root,
                         text="Pause",
                         height=3,
                         font="Arial 12 bold",
                         highlightbackground="purple",
                         highlightthickness="10",
                         fg="black",
                         command=pause_music)

# unpause
"""unpause_button = tk.Button(root,
                           text="Unpause",
                           height=3,
                           font="Arial 12 bold",
                           highlightbackground="yellow",
                           highlightthickness="10",
                           fg="black",
                           command=unpause_music)"""

# place the name of the song
song_name = tk.StringVar()
song_label = tk.Label(root,
                      font="Arial 12 bold",
                      textvariable=song_name)
song_label.pack()

# place the buttons
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
'''unpause_button.pack(fill="x")'''
play_list.pack(fill="both", expand="True")
play_list.bind("<<ListboxSelect>>", play_music_selection)

root.mainloop()
