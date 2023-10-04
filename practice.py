import math

# 14
# accepts a sentence
# calculate number of upper and lower case letters

sentence = input("Give me a sentence: ")
countUpper = 0
countLower = 0

for character in sentence:
    if character.isupper():
        countUpper += 1
    elif character.islower():
        countLower += 1

print("Number of upper case characters: ", countUpper)
print("Number of lower case characters: ", countLower)
