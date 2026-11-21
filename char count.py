text= input("Enter a string: ")
while True:
    char= input("Enter the charecter to count: ")
    if len(char)==1:
        break
    else:
        print("Please enter a single charecter")

counter= text.count(char)
print("The charecter",char,"occurs",counter,"times")
