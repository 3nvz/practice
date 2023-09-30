import math

# 6
# input into array
# loop through array and perform math ops
# append to array and print

def mathOperation():
    result = []
    items = [int(x) for x in input("Give me comma seperated numbers: ").split(",")]
    print(items)
    for d in items:
        result.append(str(math.floor(math.sqrt((2 * 50 * d)/30))))
    
    commaSepOutput = ','.join(result)
    print(commaSepOutput)

mathOperation()