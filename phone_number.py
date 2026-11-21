print("Enter the phone number in this format: XXX-XXX-XXXX")
number = input("Enter the Phone number: ").strip()
flag = True
reason=""
if number.count("-")!=2:
    flag=False
    reason="Wrong number of ddashes"
else:
    if len(number)!=12:
        flag = False
        reason="The number entered is not 10 digits"
    else:
        if number[3]!="-" or number[7]!="-":
            flag = False
            reason="Dashes arent in the right places"
        else:
            _number=number.split("-")
            if _number[2].isdigit()==False or _number[1].isdigit()==False or _number[0].isdigit()==False:
                flag=False
                reason="The entered number contains other charcters in the place of numbers"

if flag==True:
    print("Valid number")
else:
    print(f"Number is not valid.\nReason: {reason}")
