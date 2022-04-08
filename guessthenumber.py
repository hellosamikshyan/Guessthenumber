#here we go with our new project guess the number

from numpy import true_divide
import random


print("Welcome to the guess the number game")
play=input("Do you want to play?")
if play!="yes":
    exit()
print("Ok let's play")


choice=1
number=random.randint(5,8)

while True:
    print("ENTER THE NUMBER")
    num=int(input())
    if num==number:
        print("congrat's you have win the match")
        exit()
    elif num>number:
        print("Enter a lower number that's too high")
    elif num<number:
        print("Enter greater number that's too low")
    else:
        print("something went wrong")
    choice=choice+1
    if choice>6:
        print("Your moves is our now ")
        exit()
        