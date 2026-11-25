# program to print * instead of vowels
str = input("Enter a string please: ")
compare = "AEIOUaeiou"
str2=""
for i in str:
    if i in compare:
       str2+="*"
    else:
       str2=str2 + i

print(f"The modified string is: {str2}")
