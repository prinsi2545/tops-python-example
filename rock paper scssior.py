import random

l=["rock","paper","scissor"]
computer=random.choice(l)

user=input("choice (rock,paper,scissor):")

if user==computer:
    print("draw")
elif user=="rock" and computer=="paper":
    print("computer wins")
elif user=="paper" and computer=="scissor":
    print("computer wins")
elif user=="scissor" and computer=="rock":
    print("computer wins")
elif user=="paper" and computer=="rock":
    print("user wins")
elif user=="scissor" and computer=="paper":
    print("user wins")
elif user=="rock" and computer=="scisoor":
    print("user wins")
