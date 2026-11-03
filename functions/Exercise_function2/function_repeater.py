def repeat(times):
    def decorator(func):
        results = []
        def wrapper(*args, **kwargs):
            nonlocal results
            for i in range(times):
               results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


def print_result():
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args,**kwargs)
            print(result)
        return wrapper
    return decorator

@print_result()
@repeat(5)
def square(x):
    return x * x

square(4)
# [16, 16, 16]