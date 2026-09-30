# Vocabulary overlap between two sentences

# You are given two sentences:

# sentence_a = "the quick brown fox jumps over the lazy dog"
# sentence_b = "the lazy cat sleeps while the quick dog watches"

# Split each into a set of words. Compute and print the common words, the words unique to each sentence, and the full combined vocabulary. Then compute and print the overlap ratio: the number of common words divided by the number of total unique words (as a "x/y" string).

sentence_a = "the quick brown fox jumps over the lazy dog"
sentence_b = "the lazy cat sleeps while the quick dog watches"

words_a = set(sentence_a.split())
words_b = set(sentence_b.split())

common_words = words_a & words_b
unique_to_a = words_a - words_b
unique_to_b = words_b - words_a
combined_vocabulary = words_a | words_b
overlap_ratio = f"{len(common_words)}/{len(combined_vocabulary)}"

print("Common words:", common_words)
print("Only in sentence A:", unique_to_a)
print("Only in sentence B:", unique_to_b)
print("Combined vocabulary:", combined_vocabulary)
print("Overlap ratio:", overlap_ratio)
