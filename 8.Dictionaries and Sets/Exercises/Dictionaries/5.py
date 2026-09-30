# Manual word frequency

# You are given the following paragraph:

# paragraph = "The rain in Spain falls mainly on the plain. The plain is flat, and the rain is steady."

# Split it into words, strip out any non-alphabetic characters from each word (do not use string.punctuation or regular expressions), and build a frequency dictionary. Then find the most frequent word.

paragraph = "The rain in Spain falls mainly on the plain. The plain is flat, and the rain is steady."

word_frequencies = {}

for word in paragraph.split():
	cleaned_word = "".join(character for character in word if character.isalpha()).lower()
	if cleaned_word:
		word_frequencies[cleaned_word] = word_frequencies.get(cleaned_word, 0) + 1

most_frequent_word = max(word_frequencies, key=word_frequencies.get)

print(word_frequencies)
print(f"Most frequent word: {most_frequent_word} ({word_frequencies[most_frequent_word]} times)")