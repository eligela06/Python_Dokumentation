# Manual word frequency

# You are given the following paragraph:

# paragraph = "The rain in Spain falls mainly on the plain. The plain is flat, and the rain is steady."

# Split it into words, strip out any non-alphabetic characters from each word (do not use string.punctuation or regular expressions), and build a frequency dictionary. Then find the most frequent word.


paragraph = "The rain in Spain falls mainly on the plain. The plain is flat, and the rain is steady."

words = paragraph.split()
frequenzy = {}

clean_words = []


for word in words:
    clean_word = ""
    for letter in word:
        if letter.isalpha():
            clean_word += letter
    clean_words.append(clean_word)

for word in clean_words:
    if word not in frequenzy:
        frequenzy[word] = 1
    else:
        frequenzy[word] += 1

top = max(frequenzy, key = frequenzy.get)
print(top)
print(frequenzy)