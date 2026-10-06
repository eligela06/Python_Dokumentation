# Start with an empty list squares = []. Write a program that iterates over all the numbers between 1 and 5, and computes their square. Save both the number and its square into a tuple, and save all the tuples in a list.
# At the end of the program, squares should be:
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# squares = []
# for i in range(1,6):
#     squares.append((i, i * i))

# print(squares)

squares = [(i,i * i) for i in range(1,6)]
print(squares)