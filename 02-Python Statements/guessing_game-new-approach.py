import random
num = int(random.randint(1,100)) 
print(num)
guess = int(input("Pick a number: ")) # get a guess
if abs(guess - num) <= 10: # is the guess warm or cold?
	print("WARM!")
else:
    print("COLD")
if guess == num:
    print("You got it! The number is %d! " % (num))
previous = guess # initilize the previous vairable for later
guess_count = int(1)
while guess != num: # loop until correct: 
    guess_count += 1
    guess = int(input("Pick another number: ")) # get a guess 
    if guess == num: #  is it correct?
        print("You've won! The number is %d! " % (guess)) # announce the guess count
        print("It took you %d tries, but you got it. Congrats! " % (guess_count))
        break # leave the loop
    diff_current = abs(guess - num)
    diff_prev = abs(previous - num)
    if diff_current <= diff_prev:
        print("Warmer: You are closer now than before")
    if diff_prev <= diff_current:        
        print("Colder: You are farther away now than before")
    if guess <= 0:
        print("Out of Bounds. Try again.")
    if guess > 100:
        print("Out of Bounds. Try again.")
    previous = guess #save the guess as previous
