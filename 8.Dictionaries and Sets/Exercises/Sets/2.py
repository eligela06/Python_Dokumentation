# ou are given two sentences:

# sentence_a = "the quick brown fox jumps over the lazy dog"
# sentence_b = "the lazy cat sleeps while the quick dog watches"

# Split each into a set of words. Compute and print the common words, the words unique to each sentence, and the full combined vocabulary. Then compute and print the overlap ratio: the number of common words divided by the number of total unique words (as a "x/y" string).
{'lazy', 'jumps', 'while', 'sleeps', 'quick', 'the', 'fox', 'over', 'cat', 'watches', 'dog', 'brown'}

sentence_a = "the quick brown fox jumps over the lazy dog"
sentence_b = "the lazy cat sleeps while the quick dog watches"

sentence_a = set(sentence_a.split())
sentence_b = set(sentence_b.split())

only_in_a = (sentence_a - sentence_b)
only_in_b = (sentence_b - sentence_a)
vocabulary = (sentence_a | sentence_b)
common_words = sentence_a & sentence_b
overlap_ratio = f"{len(common_words)}/{len(vocabulary)}"

print("Common words:", common_words)
print("Only in sentence_a:", only_in_a)
print("Only in sentence_b:", only_in_b)
print("Vocabulary:", vocabulary)
print("Overlap ratio:", overlap_ratio)