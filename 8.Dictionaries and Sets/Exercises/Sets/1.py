raw_tags = ["python", "coding", "python", "beginner", "coding", "tutorial"]

tags = set(raw_tags)
tags.add("dictionaries")

if "beginner" in tags:
	tags.remove("beginner")

tags.discard("advanced")
popped_tag = tags.pop()

print(popped_tag)
print(tags)

# Build a set tags from raw_tags. Add the new tag "dictionaries", conditionally remove "beginner" only if present (using if/.remove()), safely discard "advanced" even though it isn't present (using .discard()), and finally .pop() an arbitrary element, printing it and the resulting set.
