def count(start=0,end=1,steps=1):
    '''
    The function count from paramether One up to parameter two
    Usage:
    print(count(1,10,2))
    output:
    [1, 3, 5, 7, 9]
    '''
    nums = []
    for i in range(start,end,steps):
        nums.append(i)
    return nums


print(count(1,10,1))

