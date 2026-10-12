# Function with parameters and conditionals
# You are given a list of ages:
# ages = [12, 18, 25, 15, 42]
# Write a function age_group(age) that returns "minor" if the age is below 18 and "adult" otherwise. Use a for loop to call the function for every age in the list and print a result like "12: minor".

ages = [12, 18, 25, 15, 42]

def age_group(age):
    if age < 18:
        return "minor"
    else:
        return "adult"

for age in ages:
    print(f"{age}: {age_group(age)}")