

#Print the Integral in a dictionary

numberForInteg = 8
dicToFill = dict()

dicToFill.update({f'{i}' : f'{i * i}' for i in range(1, numberForInteg + 1)})

print(dicToFill)
