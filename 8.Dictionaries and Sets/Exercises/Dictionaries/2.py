jan_sales = {"pen": 100, "notebook": 50, "eraser": 30}
feb_sales = {"notebook": 40, "eraser": 20, "ruler": 15}
mar_sales = {"pen": 60, "ruler": 25, "stapler": 10}


quarter_totals = {}
for month_sales in (jan_sales, feb_sales, mar_sales):
    for product, quantity in month_sales.items():
        quarter_totals[product] = quarter_totals.get(product, 0) + quantity

print(quarter_totals)

best_selling_product = max(quarter_totals, key=quarter_totals.get)
print(best_selling_product, quarter_totals[best_selling_product])
