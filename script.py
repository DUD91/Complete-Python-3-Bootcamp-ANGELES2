import random
print("Here are the rules: \n'Guess a number between 1 and 100.' \n'We'll give you a hint if you need one.'")
num = int(random.randint(1,100))
print(num)
guess_count = int(1)
guess = int(input("Guess a number! "))
while guess != num:
    guess_count = guess_count + 1
    if guess <= 0:
        print("Out of Bounds. Try again.")
    if guess > 100:
        print("Out of Bounds. Try again.")
    guess = int(input("Guess again: "))
if guess == num:
    print("You've won! It took you %d tries, but you got it. " % (guess_count))