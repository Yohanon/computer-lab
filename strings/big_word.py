sentence=input("Enter a sentence: ")
sentence = sentence.split()
big_ind = 0
big_Word=sentence[0]
for i in range(1,len(sentence)):
    if len(sentence[big_ind]) == len(sentence[i]):
        big_Word+= " & "+ sentence[i]
    elif len(sentence[big_ind]) < len(sentence[i]):
        big_Word = sentence[i]
        big_ind = i

print(f"BIGGEST WORD(S): {big_Word}")
