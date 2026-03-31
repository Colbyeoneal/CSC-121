#Using random module
import random
# List to pull from
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters_list = ["A", "B", "C", "D", "E"]

random_numbers = random.sample(numbers_list, 4)
random_letter = random.choice(letters_list)

lottery_number = random_numbers + [random_letter]
#User input 
print("Enter your lottery guess:")
guess1 = int(input("First number: "))
guess2 = int(input("Second number: "))
guess3 = int(input("Third number: "))
guess4 = int(input("Fourth number: "))
guess_letter = input("One letter: ").upper()

user_guess = [guess1, guess2, guess3, guess4, guess_letter]
# WIN and LOSS 
print("\nWinning lottery number:")
print(*lottery_number)

print("Your guess:")
print(*user_guess)

if user_guess == lottery_number:
    print("You are a winner!")
else:
    print("Sorry, you are not a winner.")