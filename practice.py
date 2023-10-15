import math
import random

# list comprehension exercise

list = [12,24,35,70,88,120,155]

result = [x for x in list if x % 5 == 0 and x % 7 == 0]

print(result)
