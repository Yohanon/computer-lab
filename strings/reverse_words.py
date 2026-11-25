sentence = input("Enter a sentence: ")
sentence = sentence.split()
reversed_sentence = list()
for i in sentence:
    reversed_sentence += i[::-1] + " "
reversed_sentence="".join(reversed_sentence)
print(f"Modified Sentence: {reversed_sentence}")
