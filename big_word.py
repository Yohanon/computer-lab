sentence=input("Enter a sentence: ")
sentence = sentence.split()
big_ind= 0
for i in range(1,len(sentence)):
    if len(sentence[i])>len(sentence[big_ind]):
        big_ind=i
print(f"BIGGEST WORD: {sentence[big_ind]}")
