def add_sprinkles(func):
    def wrapper():
        print("Sprinkles added")
        func()
    return wrapper


def add_fudge(func):
    def wrapper():
        print("Fudge added")
        func()
    return wrapper


def get_ice_cream():
    print("Here is your Icecream")

get_ice_cream()

get_ice_cream = add_fudge(get_ice_cream)
get_ice_cream()
get_ice_cream = add_sprinkles(get_ice_cream)
get_ice_cream()
get_ice_cream = get_ice_cream
get_ice_cream()
