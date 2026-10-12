# A function calls another function
# You are given a list of prices:
# prices = [20, 50, 75, 100]
# Write a function discount(price, percent) that returns the amount of the discount. Then write a function final_price(price, percent=10) that calls discount() and returns the price after the discount has been subtracted.
# Use a for loop to calculate the final price for every price in the list with a 10% discount. Print results like "Original: 50, Final: 45.0".

prices = [20, 50, 75, 100]

def discount(price, percent):
    return (price/100) * percent

def final_price(price, percent=10):
    return price - discount(price, percent)

for price in prices:
    print(f"Original: {price}, Final: {final_price(price, 10)}")