import math

# 10
# input words seperated with whitespaces
# remove duplicates and output sorted alphabetically

i = input()
words = [x for x in i.split()]
words.sort()

print(" ".join(words))

