scores = [72, 95, 58, 88, 100, 43]

def min_max(nums):
    lowest = nums[0]
    highest = nums[0]
    for number in nums:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    return lowest, highest


lowest, highest = min_max(scores)
print(lowest, highest)