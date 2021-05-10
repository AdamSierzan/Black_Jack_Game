
import tkinter
import random

root = tkinter.Tk()
root.geometry('480x460')
root.title("BlackJack")
label_nr_1 = tkinter.Label(root, text="Simple BlackJack Game")
label_nr_1.pack()

def New_Game():

    players_points = 0 
    dealers_points = 0 


    ace = [1,11]
    cards  = random.randint(1,11)

    while players_points == 0:

        first_card = random.randint(1,11)
        players_points += first_card
        print(f"Your first card is: {first_card}")

        second_card = random.randint(1,11)
        players_points += second_card
        print(f"Your second card is: {second_card}")

        dealers_first_card  = random.randint(1,11)
        dealers_points += dealers_first_card

        dealers_second_card = random.randint(1,11)
        dealers_points += dealers_second_card
        print(f"Dealers first card is: {cards}, {dealers_points}")


        
        while players_points <21:
            keep_on_playing = input(f"Your score is {players_points}. Do you want to keep on adding cards type 'Y' or 'N':" )
            next_card = random.randint(1,11)
            if keep_on_playing == "Y":
                players_points += next_card
                if players_points > 21:
                    print("You've lost")
                    break
                elif players_points == 21:
                    print("You've won!")
                    break
                else:
                    continue
                

            else:
                if dealers_points > players_points:
                    print("You've lost")
                    break
                else:
                    print("You've won")
                    break


    print(f"Your score is {players_points} and dealer's score is {dealers_points}")

start_game_button = tkinter.Button(text="Click to start", command=New_Game, fg='green' )


start_game_button.pack()
end_game_button = tkinter.Button(text="Click to quit", fg="red")
end_game_button.pack()

check_button = tkinter.Checkbutton (root, text="check")
check_button.pack()

root.mainloop()
