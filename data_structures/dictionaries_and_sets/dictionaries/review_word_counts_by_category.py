# Nested dictionaries for grouped word count

# You are given a list of (category, review_text) tuples:

# reviews = [
#   ("electronics", "great battery life"),
#   ("books", "great plot and great characters"),
#   ("electronics", "battery drains fast"),
#   ("books", "slow start but great ending"),
#   ("electronics", "great screen quality"),
# ]

# Build a category_word_counts dictionary that maps each category to another dictionary of word frequencies within that category's reviews (i.e., a dictionary of dictionaries). Print each category's two most common words along with their counts.


reviews = [
  ("electronics", "great battery life"),
  ("books", "great plot and great characters"),
  ("electronics", "battery drains fast"),
  ("books", "slow start but great ending"),
  ("electronics", "great screen quality"),
]

category_word_counts = dict()


for category, review in reviews:
    if category not in category_word_counts:
        category_word_counts[category] = {"reviews": [review]}
    else:
        category_word_counts[category]["reviews"].append(review)

print(category_word_counts)