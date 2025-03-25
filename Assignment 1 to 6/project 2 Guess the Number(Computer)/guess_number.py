import random

def guess_Number():
    randomNum=random.randint(1,10)
    print(randomNum)
    print("Wellcome to Number Guessing Game \nIf you Guess the correct Number you Win otherwise you lose")
    UserInput=0
    while UserInput!=randomNum:

        UserInput=int(input("Guess a Number between (1 to 10) : "))
        if UserInput>randomNum:
            print("Guess Again, Number is Too much low")
        elif UserInput<randomNum:
            print("Guess Again, Number is Too much High")

    print("Congratulations! You Win \nYou are Guessing the correct Number")




guess_Number()
