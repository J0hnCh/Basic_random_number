from _ast import expr
from random import randint

from setuptools.glob import escape

attempts= 0
estimate=0
number_secret= randint(1,100)
name=  input("Say you name: ")

print(f"Ok {name}, i think of a number between 1 and 100\n You have 8 attempts to guess")

while attempts< 8:
    estimate= int(input("Why is the number?: "))
    attempts += 1

    if estimate not in range(1,101):
        print("Your number is not in the range (1-100")
    elif estimate < number_secret:
        print("My number is higher")
    elif estimate > number_secret:
        print("My number is lower")
    else:
        print(f"Congratulations {name}! you guessed the number in {attempts} attempts")
        break

if estimate != number_secret:
    print(f"Sorry attempts have been exhausted. The number secret was {number_secret}")