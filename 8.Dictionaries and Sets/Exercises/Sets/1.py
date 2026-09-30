raw_tags = ["python", "coding", "python", "beginner", "coding", "tutorial"]

tags = set(raw_tags)
tags.add("dictionaries")

if "beginner" in tags:
	tags.remove("beginner")

tags.discard("advanced")
popped_tag = tags.pop()

print(popped_tag)
print(tags)

