import math  

def main():
  
    AB: float = float(input("Enter the length of side AB: "))
    AC: float = float(input("Enter the length of side AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    BC: float = math.sqrt(AB**2 + AC**2)
    print("The length of BC (Hypotenuse) is: " + str(BC))


if __name__ == '__main__':
    main()