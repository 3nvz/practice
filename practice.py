import math

# 17
# bank account transactions
# where D stands for deposit and W for withdrawal

moneyAmount = 0

while True:
    inp = input("Do you want to deposit or withdraw? ")
    values = inp.split(" ")

    op = values[0]
    amount = int(values[1])

    if op == 'D':
        moneyAmount += amount
    elif op == 'W':
        moneyAmount -= amount
    elif op == 'E':
        break
    
    print("Amount in the bank: ", moneyAmount)