
import tkinter
import random
import pygame
import BlackJack

import subprocess as sub
p = sub.Popen('./BlackJack',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()

# root = tkinter.Tk()
# root.geometry('480x460')
# root.title("BlackJack")
# label_nr_1 = tkinter.Label(root, text="Simple BlackJack Game")
# label_nr_1.pack()

# pygame.mixer.init()

# new_game = BlackJack.new_game

# start_game_button = tkinter.Button(text="Click to start", command=new_game, fg='green' )


# start_game_button.pack()
# end_game_button = tkinter.Button(text="Click to quit", fg="red")
# end_game_button.pack()

# def play():
#     pygame.mixer.music.load("/home/adanm/Desktop/Projects/Black_Jack_Game/audio/0OEX0uFyAX.ogg")
#     pygame.mixer.music.play()



# music = tkinter.Button (root, text="check", font="Helvetica", command=play)
# music.pack()

