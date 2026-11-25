#  1. Write a program to count the number of times a character occurs in the given string,
text= input("Enter a string: ")
while True:
    char= input("Enter the charecter to count: ")
    if len(char)==1:
        break
    else:
        print("Please enter a single charecter")

counter= text.count(char)
print("The charecter",char,"occurs",counter,"times")
