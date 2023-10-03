import math

# 11
# input binary numbers comma seperated
# output binary number that is dividable by 5

numbers = [x for x in input("Give me binary numbers: ").split(",")]
result = []

for num1 in numbers:
    converted = int(num1, 2)
    
    if converted % 5 == 0:
        result.append(converted)
    
print(result)
