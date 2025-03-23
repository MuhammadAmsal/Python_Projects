import random
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works
def roll_dice():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)
    total: int = dice1 + dice2
    print("Total of two dice:", total)

def main():
 
    roll_dice()
    roll_dice()
    roll_dice()
  

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()