
nested_list = [['blue', 3], ['red', 3], ['blue', 4], ['blue', 7], ['blue', 6], ['blue', 1], ['blue', 5]]

scores = set()
result = []

for i in range(len(nested_list)):
    scores.add(nested_list[i][1])
secondLowestScore = sorted(scores)[1]


for j in range(len(nested_list)):
    if nested_list[j][1] == secondLowestScore:
        result.append(nested_list[j])
    
result.sort()
print("Result", result)


print(scores)
