def negative_positive(num):
    if num < 0:
        return "negative0"
    elif num > 0:
        return "positive"
    # else:
    #     return "zero"

print(negative_positive(5))
print(negative_positive(-3))
print(negative_positive(0))