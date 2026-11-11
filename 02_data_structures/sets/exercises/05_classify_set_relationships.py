# Classifying set relationships

# You are given a list of set pairs:

# pairs = [
#       ({1, 2}, {1, 2, 3, 4}),
#       ({1, 2, 3, 4}, {1, 2}),
#       ({1, 2}, {3, 4}),
#       ({1, 2, 3}, {3, 4, 5}),
#       ({1, 2}, {1, 2}),
# ]

# For each pair, use .issubset(), .issuperset(), and .isdisjoint() to classify the relationship between the two sets as "equal", "proper subset", "proper superset", "disjoint", or "overlapping". Print the classification for every pair.

pairs = [
      ({1, 2}, {1, 2, 3, 4}),
      ({1, 2, 3, 4}, {1, 2}),
      ({1, 2}, {3, 4}),
      ({1, 2, 3}, {3, 4, 5}),
      ({1, 2}, {1, 2}),
]

for pair in pairs:
    a, b = pair
    if a == b:
        print(f"{a} and {b} are equal")
    elif a.issubset(b) and a != b:
        print(f"{a} is a proper subset of {b}")
    elif a.issuperset(b) and a != b:
        print(f"{a} is a proper superset of {b}")
    elif a.isdisjoint(b):
        print(f"{a} is disjoint {b}")
    elif a & b:
        print(f"{a} and {b} are overlapping")