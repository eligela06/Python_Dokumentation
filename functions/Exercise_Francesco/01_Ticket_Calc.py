# Determines the ticket price based on age.
def calculate_ticket_price(age):
    if age < 12:
        return 8.0
    elif age <= 64:
        return 12.0
    else:
        return 9.0

# Applies a 10% group discount when buying at least five tickets.
def calculate_group_discount(total, number_of_tickets):
    discount = 0.0
    if number_of_tickets >= 5:
        discount = round(total * 0.1, 2)
        total = total - discount
    return total, discount

# Adds the ticket prices and applies any eligible discount.
def calculate_total(prices, number_of_tickets):
    final_price = 0
    for price in prices:
        final_price += price
    sub_total = final_price
    final_price, discount = calculate_group_discount(final_price, number_of_tickets)
    return final_price, sub_total, discount


# Asks for the number of people and each person's age.
prices = []
number_of_people = int(input('Number of people: '))
for person in range(1,number_of_people+1):
    age = int(input(f'Age of person {person}: '))
    prices.append(calculate_ticket_price(age))

# Calculates and displays the prices.
total, sub_total, discount = calculate_total(prices, number_of_people)
print(f'Subtotal: {sub_total}')
print(f'Discount: {discount}')
print(f'Final Price: {total}')