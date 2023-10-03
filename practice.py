import math

# 12
# take numbers from range 2000 to 3000
# print nums where all digits are even

results = []

for i in range(2000, 3001):
    s = str(i)
    if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
        results.append(s)

print(','.join(results))
