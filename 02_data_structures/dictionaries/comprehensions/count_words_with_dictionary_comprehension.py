words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
words_count = {word: words.count(word) for word in set(words) }
print(words_count)