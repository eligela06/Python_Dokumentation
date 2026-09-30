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