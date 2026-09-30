pantry = {"egg": 6, "flour": 2, "sugar": 1, "butter": 3}
recipe = {"egg": 2, "flour": 3, "sugar": 1, "vanilla": 1}
missing = {}
taken_ingredients = {}
pantry_after = pantry.copy()

for ingredient in recipe:
    available = pantry.get(ingredient, 0)
    needed = recipe[ingredient]

    if available < needed:
        missing[ingredient] = needed - available
        used = available
    else:
        used = needed

    if ingredient in pantry:
        taken_ingredients[ingredient] = used
        pantry_after[ingredient] = available - used

print("Missing ingredients:", missing)
print("Used from pantry:", taken_ingredients)
print("Pantry after baking:", pantry_after)