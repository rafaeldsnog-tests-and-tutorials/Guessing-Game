#guess the prize
import os
import math

description = input("Description and parameter[Kg, Km, units] of the value to be guessed (do not put the value here):")
correct_value = float(input("What is the correct value for the game: "))
os.system('cls')
guesses = True
guesses_dict = {}
diff_dict = {}
while guesses == True:
    name = input("Name: ")
    guess = float(input(description + "\nGuess: "))
    os.system('cls')
    guesses_dict[name]=guess
    diff_dict[name] = math.fabs(correct_value - guess)

    guesses = input("Do you want to end the game YES[Y/y] NO[any other] ?:")
    os.system('cls')
    if guesses == "Y" or guesses == "y":
        guesses = False
    else:
        guesses = True

#Printing the result of winners
min_value = min(diff_dict.values())
dict_of_winners = {key:value for key, value in diff_dict.items() if value == min_value}

print(f"The correct value is {correct_value}")
print("The winner(s) is(are) ")
for winner in dict_of_winners:
    print(winner + " who guessed " + str(guesses_dict[winner]) + ".\n")

