sentence = input("Enter sentence(s) and hit enter to submit\nEnter your sentence here: ")
number_word=len(sentence.split())
number_characters=len(sentence)
#printing the number of words and charcter
print(f"Number of words: {number_word}")
print(f"Number of character: {number_characters}")
if number_characters !=0:
    alphanumeric_counter=0
    for i in sentence:
        if i.isalnum():
            alphanumeric_counter+=1
    print(f"Percentage of alphanumeric character: {(alphanumeric_counter/number_characters)*100}%")
