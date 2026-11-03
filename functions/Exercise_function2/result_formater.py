def format_result(prefix, suffix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'{prefix}{result}{suffix}'
        return wrapper
    return decorator

#Bonus aufgabe
def transform_result(operation):
    def decorator(func):
        def wrapper(*args, **kwargs):
            def double():
                return func(*args, **kwargs)*2
            def square():
                return func(*args, **kwargs) **2
            def negate():
                return func(*args, **kwargs) * -1
            
            if operation == "double":
                return double()
            elif operation == "square":
                return square()
            elif operation == "negate":
                return negate()
            else:
                return "Not a valid operation"
        return wrapper
    return decorator


@format_result("Result: ", "!")
@transform_result("double")
def add(a, b):
    return a + b

print(add(2,1))

