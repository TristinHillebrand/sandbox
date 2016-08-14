"""
i dont know what im doing
"""

name = input("please enter your name: ")
while len(name) == 0:
    name = input("please enter your name: ")

for i in range(0, len(name), 2):
    print(name[i], end=" ")