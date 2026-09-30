names = ["Widget", "Gadget", "Gizmo", "Doohickey", "Thingamajig"]
prices = [12.50, 45.00, 8.75, 60.00, 22.00]

inventory = dict(zip(names, prices))
discounted = {
	name: round(price * 0.9, 2) if price > 20 else price
	for name, price in inventory.items()
}

print(inventory)
print(discounted)