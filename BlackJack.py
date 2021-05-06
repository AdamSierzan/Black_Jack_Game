import random

player = 0 
dealer = 0 


cards = random.randint(1, 11)
ace = [1,11]

while player < 22:

    player += random.randint(1,11)
    print(f"Your first card is: {player}")

    player += random.randint(1,11)
    print(f"Your second card is: {player}")


    dealer += cards
    print(f"Dealers first card is: {dealer}")
    dealer += cards
    print(f"Dealers second card is: {cards}")


    keep_on_playing = input(f"Your score is {player}. Do you want to keep on adding cards type 'Y' or 'N':" )
    if keep_on_playing == "Y" and player > 21:
        print(player)
        player += cards
        print(player)
    else:
        if dealer > player or player > 21:
            print("You've lost")
            break


print(f"Your score is {player}")