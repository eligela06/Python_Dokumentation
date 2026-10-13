# Merging with accumulation

# You have three dictionaries, each mapping product names to quantities sold that month (some products repeat across months, some don't):

# jan_sales = {"pen": 100, "notebook": 50, "eraser": 30}
# feb_sales = {"notebook": 40, "eraser": 20, "ruler": 15}
# mar_sales = {"pen": 60, "ruler": 25, "stapler": 10}

# Write code that merges all three into a single quarter_totals dictionary where overlapping products have their quantities summed, not overwritten. Then find and print the best-selling product and its quantity.


jan_sales = {"pen": 100, "notebook": 50, "eraser": 30}
feb_sales = {"notebook": 40, "eraser": 20, "ruler": 15}
mar_sales = {"pen": 60, "ruler": 25, "stapler": 10}

quarter_totals = {}


for month in [jan_sales, feb_sales, mar_sales]:
    for product, price in month.items():
        if product in quarter_totals:
            quarter_totals[product] += price
        else:
            quarter_totals[product] = price


print("Total quarter:")
print(quarter_totals)

top = max(quarter_totals, key = quarter_totals.get)
  

print(top, quarter_totals[top])