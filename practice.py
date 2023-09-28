

number = input("Give me a Number ")
userInt = int(number)

if userInt % 7 == 0 and userInt % 5 != 0:
    print("success")
else:
    print("other")
