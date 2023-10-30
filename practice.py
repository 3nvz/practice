
result = {}
s = input("Enter a string: ")

for char in s:
    result[char] = result.get(char, 0) + 1

for key in result:
    print(f"{key}: {result[key]}")
