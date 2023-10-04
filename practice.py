import math

# 13
# accepts a setence with letters and digits
# calculate number of letters and digits

sentence = [x for x in input("Give me a sentence: ").split()]
countLetter = 0
countDigit = 0

for word in sentence:
    for i in range(0, len(word)):
        if word[i].isalpha():
            countLetter += 1
        elif word[i].isdigit():
            countDigit += 1

print("Number of letters: ", countLetter)
print("Number of digits: ", countDigit)
