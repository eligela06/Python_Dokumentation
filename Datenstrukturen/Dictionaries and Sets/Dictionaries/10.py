# Inverted index (mini search engine)

# You are given a list of documents:

# documents = [
#    "the cat sat on the mat",
#    "the dog chased the cat",
#    "cats and dogs are friends",
#    "the mat was chewed by the dog",
# ]

# Build an index dictionary mapping each word to the set of document indices (using enumerate()) in which it appears. Then, given the query:

# query_words = {"the", "cat"}

# compute the set of document indices that contain all of the query words (i.e., the intersection of their posting sets), handling the case where a query word never appears in any document. Finally, build a frozen_index where every posting set is converted to a frozenset.


documents = [
   "the cat sat on the mat",
   "the dog chased the cat",
   "cats and dogs are friends",
   "the mat was chewed by the dog",
]
