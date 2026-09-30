catalog = {
  "pen": (1.50, 200),
  "notebook": (3.00, 80),
  "backpack": (45.00, 15),
  "laptop": (899.00, 4),
  "eraser": (0.50, 150),
}
total_value = 0

for product in catalog:
    total_value += catalog[product][0] * catalog[product][1]

print(total_value)

for product in catalog:
    if catalog[product][0]<5:
        classify = "budget"
    elif catalog[product][0]<100:
        classify = "standard"
    else:
        classify = "premium"
    print(product, classify)