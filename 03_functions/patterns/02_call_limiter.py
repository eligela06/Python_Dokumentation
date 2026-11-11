def limit_calls(func, max_calls):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        if count >= max_calls:
            return None
        count += 1
        return func(*args, **kwargs)
    return wrapper


def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b

limited = limit_calls(calculate, 3)

print(limited(4, 5))                        # 9
print(limited(4, 5, operation="multiply"))  # 20
print(limited(a=10, b=20))                  # 30
print(limited(100, 200))                    # None
