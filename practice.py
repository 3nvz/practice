import math

# 9
# Accept sequenece of lines as input
# output all capital

lines = []

while True:
    inputToCapitalize = input()

    if inputToCapitalize:
        lines.append(inputToCapitalize.upper())
    else:
        break

for sentence in lines:
    print(sentence)

