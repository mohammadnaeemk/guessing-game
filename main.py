# guessing game
import random
#variables

number = random.randint(0,101)
userNumber = int(input("please guess a number : "))
while True :
    if userNumber == number:
        print("you guessed correctly. you win!")
        break
    elif userNumber > number:
        print("Your number is greater than the random number!")
        userNumber = int(input("please guess a number : "))
    elif userNumber < number:
        print("Your number is less than the random number!")
        userNumber = int(input("please guess a number : "))

