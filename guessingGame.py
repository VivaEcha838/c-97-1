import random
chances = 0

number = random.randint(1,9)



while chances < 5: 
    guess = int(input("Enter your guess : "))
    
    
    
    if guess == number:
        print("Congrats! You WIN")
        break
    elif guess < number:
        print("Good try. Your guess is smaller than the random number. Try a number higher")
    else:
        print("Your guess is greater than the random number. Try a number lower.")
    chances = chances+1
    if not chances < 5:
        print("Sorry, you lose. The number is: ", number)
    