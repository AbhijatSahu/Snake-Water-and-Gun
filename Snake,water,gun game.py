import random

print('''choose:
s for snake
w for water
g for gun''')
li = ["s", "w", "g"]

choice_of_computer = random.choice(li)
# taking valid user input
while (1):
    user_input = input("your choice:")
    if (user_input != "s" and user_input != "w" and user_input != "g"):
        print("invalid input")
        continue
    else:
        break

# function to choose winner
def winorlose(a, b):
    if (a == "s" and b == "g"):
        return "YOU WIN!"
    if (a == "w" and b == "s"):
        return "YOU WIN!"
    if (a == "g" and b == "w"):
        return "YOU WIN!"
    if (a == b):
        return "DRAW!"
    return "YOU LOSE!"

# result
result = winorlose(choice_of_computer, user_input)
print("choice of computer:", choice_of_computer)
print(result)