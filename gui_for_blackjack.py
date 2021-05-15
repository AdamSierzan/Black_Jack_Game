
import tkinter
import random
from tkinter.constants import WORD
from typing import Text
import pygame
import BlackJack
import tkinter.messagebox

root = tkinter.Tk()
root.geometry('480x460')
root.title("BlackJack")
label_nr_1 = tkinter.Label(root, text="Simple BlackJack Game")
label_nr_1.pack()

pygame.mixer.init()

# new_game = BlackJack.new_game
tkinter.messagebox.showinfo("Welcome to My Game")

start_game_button = tkinter.Button(text="Click to start", command=BlackJack.new_game, fg='green' )


start_game_button.pack()
end_game_button = tkinter.Button(text="Click to quit", command=root.destroy, fg="red")
end_game_button.pack()

def play():
    pygame.mixer.music.load("/home/adanm/Desktop/Projects/Black_Jack_Game/audio/0OEX0uFyAX.ogg")
    pygame.mixer.music.play()



# txt = tkinter.Text(root, width=30, height=10, wrap=WORD)
# txt.pack()

music = tkinter.Button (root, text="check", font="Helvetica", command=play)
music.pack()





root.mainloop()
