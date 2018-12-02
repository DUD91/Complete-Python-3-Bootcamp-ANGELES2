import random
num = int(random.randint(1,100)) 
print(num)
guess = int(input("Pick a number")) # get a guess
if abs(guess - num) <= 10: # is the guess warm or cold?
	print("WARM!")
else:
    print("COLD")
previous = guess # save the guess as previous
while guess != num: # loop until correct: 
    guess = int(input("Pick another number")) # get a guess 
    if guess == num: #  is it correct?
        print("You've won! The number is %d! " % (guess)) # announce the guess count
        break # leave the loop
        ''' ugh:
    if warmer: 
        print("Warmer")
    if colder:
        print("Colder")
    '''
    elif guess <= 0:
        print("Out of Bounds. Try again.")
    elif guess > 100:
        print("Out of Bounds. Try again.")
    guess = previous #save the guess as previous
