# Adds the prices of all ordered items.
def calculate_subtotal(prices):
    subtotal = 0
    for price in prices:
        subtotal += price
    return subtotal

# Calculates the tip based on the subtotal.
def calculate_tip(subtotal, tip_percent):
    return subtotal * (tip_percent/100)

# Calculates the tax based on the subtotal.
def calculate_tax(subtotal, tax_percent):
    return subtotal * (tax_percent/100)

# Adds the subtotal, tip, and tax.
def calculate_total(subtotal, tip, tax):
    return subtotal + tip + tax

# Splits the total evenly among all people.
def calculate_per_person(total, number_of_people):
    return total / number_of_people

# Calculates all amounts and prints the formatted receipt.
def print_receipt(prices, tip_percent, tax_percent, number_of_people):
    sub_total = calculate_subtotal(prices)
    tip = calculate_tip(sub_total, tip_percent)
    tax = calculate_tax(sub_total, tax_percent)
    total = calculate_total(sub_total, tip, tax)
    per_person = calculate_per_person(total, number_of_people)

    print(f'Subtotal: {sub_total:.2f}')
    print(f'Tip: {tip:.2f}')
    print(f'Tax: {tax:.2f}')
    print(f'Total: {total:.2f}')
    print(f'Each person pays: {per_person:.2f}')

# Collects item prices, tip, tax, and the number of people.
items_price = []

amount_items = int(input('How many items did you order: '))

for item in range(1,amount_items+1):
    items_price.append(float(input(f'What is the price of Item {item}: ')))

tip = int(input('How many percent tip you wanna give: '))
tax = int(input('What is the amount of tax(in percent): '))
number_of_people = int(input('Number of people splittion the Bill: '))

# Prints the receipt using the entered values.
print_receipt(items_price, tip, tax, number_of_people)