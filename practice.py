import math

# 14
# accepts a sentence
# calculate number of upper and lower case letters

sentence = input("Give me a sentence: ")
countUpper = 0
countLower = 0

for letter in sentence:
    if letter.isupper():
        countUpper += 1
    elif letter.islower():
        countLower += 1

print("Number of upper case letter: ", countUpper)
print("Number of lower case letter: ", countLower)
