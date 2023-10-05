import math

# 16
# comma seperated input of ints saved in a list
# output all odd ints comma seperated

numbers = [int(x) for x in input("Give me comma seperated numbers: ").split(",")]
results = []

for num in numbers:
    if num % 2 != 0:
        results.append(str(num))
print(','.join(results))