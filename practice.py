import math

# Accept strings, but only print numbers

s = [x for x in input("Give me sth: ").split()]
result = []

for i in s:
    if i.isdigit():
        result.append(i)

print(result)