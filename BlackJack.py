import random

player = 0 
dealer = 0 


cards = random.randint(1, 11)
ace = [1,11]

while True:
    player += cards
    print(f"Your first card is: {player}")

    player += cards
    print(f"Your second card is: {player}")


    dealer += cards
    print(f"Dealers first card is: {dealer}")
    dealer += cards

    keep_on_playing = input("Do you want to keep on adding cards type 'Y' or 'N':" )
    if keep_on_playing == "Y":
        player += cards
        if player > 21:
            print ("You've lost")
            break
        else:
            print(f"Your score now is : {player}")
            continue
        
    
    if player > 21:
        print("You've lost")
        break
print(f"Your score is{player}")