numbers = [1,4,5,98,21]
def min_max(nums):
    min = nums[0]
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
        elif num < min:
            min = num
    return min, max

min, max = min_max(numbers)
print(type(min_max(numbers)))