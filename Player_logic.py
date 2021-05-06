import random

player = 0 


cards = random.randint(1, 11)
ace = [1,11]

while player ==0:

    player += cards
    print(f"Your first card is: {player}")

    player += cards
    print(f"Your second card is: {player}")


    if player < 22:
        keep_on_playing = input(f"Your score is {player}. Do you want to keep on adding cards type 'Y' or 'N':" )
        if keep_on_playing == "Y":
            player += cards
            if player < 22:
                keep_on_playing = input(f"Your score is {player}. Do you want to keep on adding cards type 'Y' or 'N':" )
            elif player == 21:
                print("You've won!")
            else:
                print("You've lost")
                break
    
    elif player == 21:
        print("You've won!")

    else:
        print("You've lost")
        break
  
    
print(f"Your score is {player}")