# A multiset is like a set but keeps track of how many times each item occurs — a plain dictionary mapping each item to its count can represent one. You are given a pantry and a recipe, both represented this way:

# pantry = {"egg": 6, "flour": 2, "sugar": 1, "butter": 3}
# recipe = {"egg": 2, "flour": 3, "sugar": 1, "vanilla": 1}

# Using only dictionaries, loops, and conditionals, determine: (a) which ingredients (and how much of each) are missing from the pantry to make the recipe (only include ingredients where the recipe needs more than the pantry has), (b) how much of each ingredient the recipe would actually use from the pantry (the smaller of the two counts, for ingredients present in both), and (c) what the pantry would look like after baking if missing ingredients are simply ignored (subtract what the recipe uses, never going below zero).


pantry = {"egg": 6, "flour": 2, "sugar": 1, "butter": 3}
recipe = {"egg": 2, "flour": 3, "sugar": 1, "vanilla": 1}


missing = dict()
used = dict()
remaining = dict()

for element, amount in recipe.items():
    if element not in pantry:
        missing[element] = amount
        continue

    if amount > pantry[element]:
        missing[element] = amount - pantry[element]
        used[element] = pantry[element]
    else:
        used[element] = amount

for element, amount in pantry.items():
    if element in used:
        remaining[element] = amount - used[element]
    else:
        remaining[element] = amount

print("Missing:", missing)
print("Used:", used)
print("Remaining:", remaining)