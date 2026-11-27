print("----------------------------------------Welcome to Calculator---------------------")
def instructions():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division(quotient)")
    print("5. Division(remainder)")
    print("6. Instructions")
    print("0. Exit")

instructions()

while(True):
    try:
        choice = int(input("Enter the operation you want to perform: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if choice > 0 and choice <6:
        while(True):
            try:
                a = int(input("Enter the first number: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            break
        while(True):
            try:
                b = int(input("Enter the secound number: "))
            except ValueError:
                print("Please enter a valid number")
                continue
            break
        if choice == 1:
            print("Sum: ",a+b)
        elif choice == 2:
            print("Differnce: ",a-b)
        elif choice == 3:
            print("Product: ",a*b)
        elif choice == 4:
            if b != 0:
                print("Quotient: ",a//b)
            else:
                print("Division by zero is not allowed")
        elif choice == 5:
            if b!=0:
                print("Remainder: ",a%b)
            else:
                print("Division by Zero is not allowed")
    elif choice == 6:
        instructions()
    elif choice == 0:
        print("Havve a great time please vist us again")
        break
    else:
        print("Please enter a valid number, TRY AGAIN")
