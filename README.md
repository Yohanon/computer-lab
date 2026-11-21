# Computer Lab - Python Exercises

This repository contains Python solutions for computer lab exercises covering string operations, validation, and parsing.

---

## Question 1: Character Occurrence Counter

**Problem Statement:**
Write a program to count the number of times a character occurs in the given string.

### Code: `char_count.py`
```text
───────┬────────────────────────────────────────────────────────────────────────
       │ File: char_count.py
───────┼────────────────────────────────────────────────────────────────────────
   1 + │ #  1. Write a program to count the number of times a character occurs in the given string,
   2   │ text= input("Enter a string: ")
   3   │ while True:
   4   │     char= input("Enter the charecter to count: ")
   5   │     if len(char)==1:
   6   │         break
   7   │     else:
   8   │         print("Please enter a single charecter")
   9   │ 
  10   │ counter= text.count(char)
  11   │ print("The charecter",char,"occurs",counter,"times")
───────┴────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter a string: hello world
Enter the charecter to count: l
The charecter l occurs 3 times
```

---

## Question 2: Replace Vowels with Asterisks

**Problem Statement:**
Write a program which replaces all vowels in the string with '*'.

### Code: `star_vowel.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: star_vowel.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ # program to print * instead of vowels
   2 │ str = input("Enter a string please: ")
   3 │ compare = "AEIOUaeiou"
   4 │ str2=""
   5 │ for i in str:
   6 │     if i in compare:
   7 │        str2+="*"
   8 │     else:
   9 │        str2=str2 + i
  10 │ 
  11 │ print(f"The modified string is: {str2}")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter a string please: Computer Science
The modified string is: C*mp*t*r Sc**nc*
```

---

## Question 3: Reverse String into New String

**Problem Statement:**
Write a program which reverses a string and stores the reversed string in a new string.

### Code: `rev_str.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: rev_str.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ # Take input from user
   2 │ original_string = input("Enter a string: ")
   3 │ 
   4 │ # Initialize an empty string to store reversed characters
   5 │ reversed_string = ""
   6 │ 
   7 │ # Loop through each character and prepend it to the new string
   8 │ for char in original_string:
   9 │     reversed_string = char + reversed_string
  10 │ 
  11 │ # Display the results
  12 │ print("Original string:", original_string)
  13 │ print("Reversed string:", reversed_string)
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter a string: Python Programming
Original string: Python Programming
Reversed string: gnimmargorP nohtyP
```

---

## Question 4: Phone Number Format Validator

**Problem Statement:**
Write a program that prompts for a phone number of 10 digits and two dashes, with dashes after the area code and the next three numbers. For example, 017-555-1212 is a legal input. Display if the phone number entered is valid format or not and display if the phone number is valid or not (i.e., contains just the digits and dash at specific places).

### Code: `phone_number.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: phone_number.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ print("Enter the phone number in this format: XXX-XXX-XXXX")
   2 │ number = input("Enter the Phone number: ").strip()
   3 │ flag = True
   4 │ reason=""
   5 │ if number.count("-")!=2:
   6 │     flag=False
   7 │     reason="Wrong number of ddashes"
   8 │ else:
   9 │     if len(number)!=12:
  10 │         flag = False
  11 │         reason="The number entered is not 10 digits"
  12 │     else:
  13 │         if number[3]!="-" or number[7]!="-":
  14 │             flag = False
  15 │             reason="Dashes arent in the right places"
  16 │         else:
  17 │             _number=number.split("-")
  18 │             if _number[2].isdigit()==False or _number[1].isdigit()==False or _number[0].isdigit()==False:
  19 │                 flag=False
  20 │                 reason="The entered number contains other charcters in the place of numbers"
  21 │ 
  22 │ if flag==True:
  23 │     print("Valid number")
  24 │ else:
  25 │     print(f"Number is not valid.\nReason: {reason}")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter the phone number in this format: XXX-XXX-XXXX
Enter the Phone number: 017-555-1212
Valid number
```

---

## Question 5: Sentence Statistics

**Problem Statement:**
Write a program that should prompt the user to type some sentence(s) followed by “enter”. It should then print the original sentence(s) and the following statistics relating to the sentence(s) :
    1. Number of words
    2. Number of characters (including white-space and punctuation)
    3. Percentage of characters that are alphanumeric

### Code: `sentence.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: sentence.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ sentence = input("Enter sentence(s) and hit enter to submit\nEnter your sentence here: ")
   2 │ number_word=len(sentence.split())
   3 │ number_characters=len(sentence)
   4 │ #printing the number of words and charcter
   5 │ print(f"Number of words: {number_word}")
   6 │ print(f"Number of character: {number_characters}")
   7 │ if number_characters !=0:
   8 │     alphanumeric_counter=0
   9 │     for i in sentence:
  10 │         if i.isalnum():
  11 │             alphanumeric_counter+=1
  12 │     print(f"Percentage of alphanumeric character: {(alphanumeric_counter/number_characters)*100}%")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter sentence(s) and hit enter to submit
Enter your sentence here: Hello, World! 123
Number of words: 3
Number of character: 17
Percentage of alphanumeric character: 76.47058823529412%
```

---

## Question 6: Formula Bracket Matcher

**Problem Statement:**
Write a program to input a formula with some brackets and checks, and prints out if the formula has the same number of opening and closing parentheses.

### Code: `formula.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: formula.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ exprestion=input("Enter your formula: ")
   2 │ left_closing_bracket = exprestion.count("(")
   3 │ right_closing_bracket = exprestion.count(")")
   4 │ if left_closing_bracket == right_closing_bracket:
   5 │     print("The formula has same number of opening and closing paranthesis")
   6 │ else:
   7 │     print("The formula has different number of opening and closing pranthesis\nFormula is invalid")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter your formula: (a + b) * (c + d)
The formula has same number of opening and closing paranthesis
```

---

## Question 7: Vowel Counter

**Problem Statement:**
Write a program that inputs a line of text and prints out the count of vowels in it.

### Code: `vowel_count.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: vowel_count.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ s=input("Enter your string: ").upper()
   2 │ vowel="AEIOU"
   3 │ vowel_counter=0
   4 │ for i in s:
   5 │     if i in vowel:
   6 │         vowel_counter+=1
   7 │ print(f"The number of vowels: {vowel_counter}")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter your string: Artificial Intelligence
The number of vowels: 10
```

---

## Question 8: Find Biggest Word(s)

**Problem Statement:**
Write a program to input a line of text and print the biggest word (length wise) from it.

### Code: `big_word.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: big_word.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ sentence=input("Enter a sentence: ")
   2 │ sentence = sentence.split()
   3 │ big_ind = 0
   4 │ big_Word=sentence[0]
   5 │ for i in range(1,len(sentence)):
   6 │     if len(sentence[big_ind]) == len(sentence[i]):
   7 │         big_Word+= " & "+ sentence[i]
   8 │     elif len(sentence[big_ind]) < len(sentence[i]):
   9 │         big_Word = sentence[i]
  10 │         big_ind = i
  11 │ 
  12 │ print(f"BIGGEST WORD(S): {big_Word}")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter a sentence: python data structures and algorithms
BIGGEST WORD(S): structures & algorithms
```

---

## Question 9: Reverse Each Word in Sentence

**Problem Statement:**
Write a program to input a line of text and create a new line of text where each word of input line is reversed.

### Code: `reverse_words.py`
```text
─────┬──────────────────────────────────────────────────────────────────────────
     │ File: reverse_words.py
─────┼──────────────────────────────────────────────────────────────────────────
   1 │ sentence = input("Enter a sentence: ")
   2 │ sentence = sentence.split()
   3 │ reversed_sentence = list()
   4 │ for i in sentence:
   5 │     reversed_sentence += i[::-1] + " "
   6 │ reversed_sentence="".join(reversed_sentence)
   7 │ print(f"Modified Sentence: {reversed_sentence}")
─────┴──────────────────────────────────────────────────────────────────────────
```

### Terminal Output
```text
Enter a sentence: hello world from python
Modified Sentence: olleh dlrow morf nohtyp 
```

