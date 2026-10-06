# Tuple values

# You are given a catalog dictionary mapping product names to (price, quantity) tuples:

# catalog = {
#   "pen": (1.50, 200),
#   "notebook": (3.00, 80),
#   "backpack": (45.00, 15),
#   "laptop": (899.00, 4),
#   "eraser": (0.50, 150),
# }

# Compute the total inventory value (price × quantity, summed over all products). 
# Then, for each product, classify it by its price as "budget" (< $5), "standard" (< $100), or "premium" (otherwise), printing each product with its tier.


catalog = {
  "pen": (1.50, 200),
  "notebook": (3.00, 80),
  "backpack": (45.00, 15),
  "laptop": (899.00, 4),
  "eraser": (0.50, 150),
}

inventory_value = 0

for product, (price, quantity) in catalog.items():
    inventory_value += price * quantity

    if price < 5:
        tier = "budget"
    elif price < 100:
        tier = "standard"
    else:
        tier = "premium"

    print(product, tier)

print("Total inventory value:", inventory_value)