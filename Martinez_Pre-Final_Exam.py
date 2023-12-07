print("CS112: COMPUTER PROGRAMMING 1 - PRE FINAL EXAM")
print("Created by: Thomas Gabriel D. Martinez")
print()
print("Problem: Create python program that displays all prime numbers within a range:")
print()
print("RULES TO CONSIDER:")
print("[1] If number[start] is a negative number. The program will prompt a message: 'Enter a non-negative number'")
print("[2] If number[end] is less than number[start]. The program will prompt a message: 'Enter a number greater than number[start]'")
print("[3] Enter the number '0', to terminate the program.")
print()


def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


while True:
    startNum = int(input("Enter a number [start]: "))
    if startNum == 0:
        print("\n\tProgram terminated.")
        break
    endNum = int(input("Enter a number [end]  : "))

    if startNum < 0:
        print("\nEnter a non-negative number!!\n")
        continue
    elif endNum < startNum:
        print(f"\nEnter a number in [end] greater than {startNum}\n")
        continue
    else:
        print(f"\nPrime numbers between {startNum} and {endNum} are:")
        for x in range(startNum, endNum + 1):
            if prime(x):
                print(x, end=' ')
        print("\n")
