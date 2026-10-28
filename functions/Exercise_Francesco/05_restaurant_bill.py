def calculate_subtotal(prices):
    subtotal = 0
    for price in prices:
        subtotal += price
    return subtotal

def calculate_tip(subtotal, tip_percent):
    return subtotal * (tip_percent/100)

def calculate_tax(subtotal, tax_percent):
    return subtotal * (tax_percent/100)

#The function calculate_tip and calculate_tax do exactly the same we can make out of two function one
#calculate(subtotal, tax_or_tip):
#   return subtotal * (tax_or_tip/100)

def calculate_total(subtotal, tip, tax):
    return subtotal + tip + tax

def calculate_per_person(total, number_of_people):
    return total / number_of_people

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
    print(f'Each person pays: {per_person:.2f}') #:.2f round the float to 2 decimals

items_price = []

amount_items = int(input('How many items did you order: '))

for item in range(1,amount_items+1):
    items_price.append(float(input(f'What is the price of Item {item}: ')))

tip = int(input('How many percent tip you wanna give: '))
tax = int(input('What is the amount of tax(in percent): '))
number_of_people = int(input('Number of people splittion the Bill: '))

print_receipt(items_price, tip, tax, number_of_people)