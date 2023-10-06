import math

# 18
# check a password for various factors
# put some password policy in place

def contains_digits(pwd):
    return any(char.isdigit() for char in pwd)

def contains_lowercase(pwd):
    return any(char.isalpha() for char in pwd)

def contains_upperCase(pwd):
    return any(char.isupper() for char in pwd)

def contains_special(pwd):
    return '@' in pwd or '#' in pwd or '$' in pwd


passwords = [x for x in input("Give me some passwords: ").split(",")]


for pwd in passwords:
    if len(pwd) > 6 and len(pwd) <= 12:
        if contains_digits(pwd) and contains_lowercase(pwd) and contains_upperCase(pwd) and contains_special(pwd):
            print(f"The password '{pwd}' meets the requirements.")
        else:
            print(f"The password '{pwd}' doesn't meet the requirements.")
    else:
        print(f"The password '{pwd}' is not long enough.")