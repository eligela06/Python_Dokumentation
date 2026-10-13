# Function that processes a list
# You are given a list of numbers:
# numbers = [4, 7, 2, 9, 12, 5, 8]
# Write a function count_even(numbers) that returns how many even numbers are in the list. Do not use any special counting functions. 
# Instead, use a loop, an if statement, and a counter variable. Print the result.

numbers = [4, 7, 2, 9, 12, 5, 8]

def count_even(numbers):
    even = 0
    for num in numbers:
        if num % 2 == 0:
            even += 1
    print(f"Even numbers: {even}")

count_even(numbers)