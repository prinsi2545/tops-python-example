import random

num=random.randint(1,20)

while True:

    guess=int(input("guess a number between 1 to 20:"))

    if guess==num:
        print("you gussed a coorect number")
        break
    elif guess>num:
        print("you guessed a greater number")
    elif guess<num:
        print("you guessed a smaales number")
        
        
