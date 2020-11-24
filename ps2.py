import random
import math 
print("Enter the range between you want to play the game")
lower_bound=int(input())
upper_bound=int(input())
number=random.randint(lower_bound,upper_bound)
guess_limit=math.ceil(math.log(upper_bound-lower_bound+1))
print(number)
print(guess_limit)


while(1):
    if guess_limit==0:
        print("You loss! Ran out of guesses")
        break
    
    print("Enter your guess")
    guess=int(input())
    

    if guess==number:
        print("You WON! your guess is correct")
        break
    elif guess>number:
        print("Your guess is more than expected answer. Try again")
    elif guess<number:
        print("Your guess is smaller than expected value. Try again")
    else:
        pass

    guess_limit=guess_limit-1
 
    print(guess_limit)


