
import tkinter

root = tkinter.Tk()
root.geometry('480x460')
root.title("BlackJack")
label_nr_1 = tkinter.Label(root, text="Simple BlackJack Game")
label_nr_1.pack()

start_game_button = tkinter.Button(text="Click to start" )

start_game_button.pack()
end_game_button = tkinter.Button(text="Click to quit")
end_game_button.pack()


root.mainloop()
