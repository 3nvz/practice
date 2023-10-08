import math

# 2.14
# accept the string "yes" in any variations as input
# otherwise print no

yes = input("Give me a yes: ").upper()

if yes == "YES":
    print("You gave me a 'yes'!")
else:
    print("no")