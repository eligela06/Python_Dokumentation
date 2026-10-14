lst = [1,2,3]
lst1 = [1,2,3]
def add_100_A(lst):
    lst.append(100)

def add_100_B(lst):
    new_lst = lst + [100]
    lst = new_lst

add_100_A(lst)
add_100_B(lst1)
print(lst,lst1)