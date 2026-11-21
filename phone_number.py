print("Enter the phone number in this format: XXX-XXX-XXXX")
number = input("Enter the Phone number: ")
flag = True

if len(number) != 12:
    print("Invalid phone number: Must be exactly 12 characters (10 digits and 2 dashes).")
    flag = False
else:
    if number[3] != "-" or number[7] != "-":
        print("Phone number is not valid: The dashes (-) are not in the correct places.")
        flag = False

    if not number[:3].isdigit() or not number[4:7].isdigit() or not number[8:].isdigit():
        print("Invalid phone number: Please enter digits and dashes only.")
        flag = False

    if flag:
        print("Number is valid")
