def append_value(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_value(1))
print(append_value(2))
print(append_value(3))