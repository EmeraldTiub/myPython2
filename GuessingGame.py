# a guessing game!
import random
the_number = random.randint(1, 9000)
guess = int(input("Guess a number between 1 and 10: "))
# start of a while loop
while guess != the_number:
# in the wile loop
# start of an if loop in the while loop (nested loop)
    if guess > the_number:
# start of a "print" of how it went ✔ or ❌ or too high or too low
        print(guess, "was too high. try again.")
# start of another if loop in the while loop (again, nested loop)
    if guess < the_number:
# a "print" again
        print(guess, "was too low. try again.")
# defining guess again
    guess = int(input("Guess again: "))
# a print by itself, not following any loop (do you see any tab on the print?) that is the clue question
print(guess, "was the number! You win! :)")
