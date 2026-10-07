# LRU cache using a plain dictionary

# Regular dictionaries remember the order in which their keys were inserted. Using only a plain dictionary (no other data structure), simulate a simple Least-Recently-Used (LRU) cache with a fixed capacity of 3, processing the following sequence of key accesses in order:

# capacity = 3
# access_sequence = ["A", "B", "C", "A", "D", "B", "E"]

# On a cache hit, "refresh" the key so it counts as most-recently-used (hint: removing and re-inserting a key moves it to the end of the dictionary's order). 
# On a cache miss, if the cache is already full, evict the oldest entry (the first key produced when iterating over the dictionary) before inserting the new key. Print the cache state after every access, labeled HIT, MISS, and EVICT as appropriate.


capacity = 3
access_sequence = ["A", "B", "C", "A", "D", "B", "E"]