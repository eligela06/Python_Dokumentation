# Function with one parameter (loop)

# You are given a list of names:
# names = [“Ann”, “Boris”, “Cathy”]
# Write a function greet(name) that prints "Hello, <name>!". Call it for every name in the list using a for loop.


names = ["Ann", "Boris", "Cathy"]

def greet(name):
    print(f'Hello {name}')

for i in names:
    greet(i)