# guessing game
import random
#variables

order = "0"
while True:
    print("Please choose the game you want : ")
    print("1_ I want to find the random number. ")
    print("2_ I want to guess the random number and the computer will find it.")
    print("3_ Exit")
    order = input("Your choice: ")
    if order == "1":
        number = random.randint(0, 100)
        userNumber = int(input("please guess a number : "))
        while True:
            if userNumber == number:
                print("you guessed correctly. you win!")
                break
            elif userNumber > number:
                print("Your number is greater than the random number!")
                userNumber = int(input("please guess a number : "))
            elif userNumber < number:
                print("Your number is less than the random number!")
                userNumber = int(input("please guess a number : "))
    elif order == "2":
        a, b = 0, 100
        print("Please choose a number between 0 and 100 in your mind and remember it. At the bottom, the computer tries to guess the number. If the guessed number is greater than your number, send the word 'more' and if it is less than your number, send 'less'. If the number is correct, send the 'ok'...")
        print("Start...")

        systemNumber = random.randint(a, b)
        print("Is the ", systemNumber, " your number?(more,less,ok) :")
        ans = input()
        while True:
            if ans == "more":
                b = systemNumber
                systemNumber = random.randint(a, b)
                print("Is the ", systemNumber, " your number?(more,less,ok) :")
                ans = input()
                continue
            elif ans == "less":
                a = systemNumber
                systemNumber = random.randint(a, b)
                print("Is the ", systemNumber, " your number?(more,less,ok) :")
                ans = input()
                continue
            elif ans == "ok":
                print("I won :)")
                break
            else:
                print("Sorry, I didn't get that.")
                ans = input("Please try again: ")
                continue
    elif order == "3":
        break
    else:
        print("Your choice is not among the options!! Please enter the correct number.")
        continue

