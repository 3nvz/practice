import math

# 8 
# comma sep input strings
# sort them alphabetically
# print them comma seperated

words = [x for x in input().split(',')]
words.sort()

print(','.join(words))
