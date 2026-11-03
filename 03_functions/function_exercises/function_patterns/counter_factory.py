def make_counter(start=0,step=1):
    def increment():
        nonlocal start, step
        start += step
        return start
    def decrement():
        nonlocal start, step
        start -= step
        return start
    def configure(new_step):
        nonlocal step
        step = new_step
        return f'New steps: {step}'
    return increment, decrement, configure

increment, decrement, configure = make_counter(start=0, step=12)

print(increment())     
print(increment())      
print(decrement())      
print(configure(5))   
print(increment())


increment1, decrement1, configure1 = make_counter(start=1, step=1)
print(increment1())
