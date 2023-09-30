import math

# 7
# take the input of 2 numbers
# generate 2 dimensional array
# growing by number of outer array

testNum1 = 3
testNum2 = 5
outerArr = []

for i in range(0, testNum1):
    innerArr = []
    for j in range(0, testNum2):
        innerArr.append(j * i)
    outerArr.append(innerArr)

print(outerArr)
