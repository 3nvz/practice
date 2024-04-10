
s = "anagram"
t = "nagaram"

dic = {"a", "b", "c", "a"}

countS, countT = {}, {}

if len(s) != len(t):
    print(False)
    

for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)
    print(countS)
