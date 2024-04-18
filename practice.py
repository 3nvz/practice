
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sumi = 0

for i in range(len(arr)):
    sumi += arr[i][-i-1]
    print(arr[i][-i-1])

print(sumi)