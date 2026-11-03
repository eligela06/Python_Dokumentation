lst = [1,2,3,4]
print(id(lst))
lst.append(5)
print(id(lst))

num = 1
print(id(num))
num += 2
print(id(num))