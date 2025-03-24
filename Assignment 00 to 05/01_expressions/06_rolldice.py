import random


def main():
    random.seed(4)
    
    # Roll die
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    
    # Get their total
    total: int = dice1 + dice2
    
    # Print out the results
    print("Dice have", 6, "sides each.")
    print("First dice:", dice1)
    print("Second dice:", dice2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()