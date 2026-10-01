# Sets
# Set methods in sequence

# You are given a list of tags with duplicates:

# raw_tags = ["python", "coding", "python", "beginner", "coding", "tutorial"]

# Build a set tags from raw_tags. Add the new tag "dictionaries", conditionally remove "beginner" only if present (using if/.remove()), safely discard "advanced" even though it isn't present (using .discard()), and finally .pop() an arbitrary element, printing it and the resulting 

raw_tags = ["python", "coding", "python", "beginner", "coding", "tutorial"]


tags = set(raw_tags)
tags.add("dictionaries")

if "beginner" in tags:
    tags.remove("beginner")

tags.discard("advanced")
print(tags.pop())
print(tags)
