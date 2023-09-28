

#Factorial of given number
#!3 3 x 2 x 1

numberToFac = 8
count = 1

for i in reversed(range(1, numberToFac + 1)):
    count *= i

print(count)
