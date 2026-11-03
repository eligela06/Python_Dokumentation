def cache_last(func):
    last_result = None
    last_arg = None

    def wrapper(x):
        nonlocal last_result, last_arg
        if x != last_arg:
            last_result = func(x)
            last_arg = x
        return last_result
        
    def clear_cache():
        nonlocal last_result, last_arg
        last_arg = None
        last_result = None
    return wrapper, clear_cache


def square(x):
    print(f"Calculating {x}")
    return x * x

cached_square, clear = cache_last(square)

print(cached_square(4))
# Calculating 4
# 16

print(cached_square(4))
# 16

print(cached_square(5))
# Calculating 5
# 25

print(cached_square(4))
# Calculating 4
# 16

clear()

print(cached_square(4))
# Calculating 4
# 16