pairs = [
	({1, 2}, {1, 2, 3, 4}),
	({1, 2, 3, 4}, {1, 2}),
	({1, 2}, {3, 4}),
	({1, 2, 3}, {3, 4, 5}),
	({1, 2}, {1, 2}),
]

for first_set, second_set in pairs:
	if first_set == second_set:
		relationship = "equal"
	elif first_set.issubset(second_set):
		relationship = "proper subset"
	elif first_set.issuperset(second_set):
		relationship = "proper superset"
	elif first_set.isdisjoint(second_set):
		relationship = "disjoint"
	else:
		relationship = "overlapping"

	print(f"{first_set} and {second_set}: {relationship}")
