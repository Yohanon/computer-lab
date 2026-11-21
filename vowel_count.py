s=input("Enter your string: ").upper()
vowel="AEIOU"
vowel_counter=0
for i in s:
    if i in vowel:
        vowel_counter+=1
print(f"The number of vowels: {vowel_counter}")
