lst = ['hi','how','are','you','?']
for index, i in enumerate(lst, start=1): #enumerate takes not only the element it also takes the index you can give the function 2 paramthers first the iterable and second the start
    print(index,i)

print()

for i in lst:
    print(lst.index(i) + 1,i)