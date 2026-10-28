def calculate_ticket_price(age):
    if age < 12:
        return 8.0
    elif age <= 64:
        return 12.0
    else:
        return 9.0

def calculate_group_discount(total, number_of_tickets):
    discount = 0.0
    if number_of_tickets >= 5:
        discount = round(total * 0.1, 2)
        total = total - discount
    return total, discount

def calculate_total(prices, number_of_tickets):
    final_price = 0
    for price in prices:
        final_price += price
    sub_total = final_price
    final_price, discount = calculate_group_discount(final_price, number_of_tickets)
    return final_price, sub_total, discount


prices = []
number_of_people = int(input('Number of people: '))

for person in range(1,number_of_people+1):
    age = int(input(f'Age of person {person}: '))
    prices.append(calculate_ticket_price(age))

total, sub_total, discount = calculate_total(prices, number_of_people)
print()
print(f'Subtotal: {sub_total}')
print(f'Discount: {discount}')
print(f'Final Price: {total}')