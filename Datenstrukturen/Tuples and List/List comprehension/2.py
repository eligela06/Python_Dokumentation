fruits = ["banana","apple","mango"]

fruits = ["banana", "apple", "mango"]

fruits_upper = [fruit.upper() if fruit[0] in ("b", "a") else fruit for fruit in fruits]

print(fruits_upper)

fruits_lower = [fruit.lower() if fruit[0] in ("B") else fruit for fruit in fruits_upper]
print(fruits_lower)