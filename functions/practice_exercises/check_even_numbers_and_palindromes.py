numbers = [4, 7, 10, 13]
words = ["radar", "python", "level", "code"]


def is_even(n):
    return n % 2 == 0


def is_palindrome(word):
    return word == word[::-1]


for number in numbers:
    print(f"{number} is even: {is_even(number)}")

for word in words:
    print(f"{word} is a palindrome: {is_palindrome(word)}")
