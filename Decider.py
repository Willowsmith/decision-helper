import random

Opt1 = input("Enter your first choice: ")
Opt2 = input("Enter your second choice: ")

if not Opt1:
    print("Please do not enter an empty value.")

if not Opt2:
    print("Please do not enter an empty value.")

result = random.choice([Opt1, Opt2])

print(result)
