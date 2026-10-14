def test(func):
    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@test
def print_somthing():
    print("Hello")

print_somthing()