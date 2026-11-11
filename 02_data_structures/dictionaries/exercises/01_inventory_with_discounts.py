# Building and transforming a dictionary

# You are given two parallel lists:

# names = ["Widget", "Gadget", "Gizmo", "Doohickey", "Thingamajig"]
# prices = [12.50, 45.00, 8.75, 60.00, 22.00]

# Combine names and prices into an inventory dictionary mapping each item to its price. 
# Then create a new discounted dictionary that applies a 10% discount (rounded to 2 decimals) to any item priced above $20, leaving other prices unchanged.

names = ["Widget", "Gadget", "Gizmo", "Doohickey", "Thingamajig"]
prices = [12.50, 45.00, 8.75, 60.00, 22.00]

inventory = dict(zip(names,prices))
discounted = {
	product: round(price * 0.9, 2) if price > 20 else price
	for product, price in inventory.items()
}
print(inventory)
print(discounted)