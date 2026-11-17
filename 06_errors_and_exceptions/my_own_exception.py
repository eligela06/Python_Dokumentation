class UppercaseException(Exception):
    pass

class lowercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']

try:
    for word in words:
        if word.isupper():
            raise UppercaseException()
        else:
            raise lowercaseException()
        
except UppercaseException:
    print("Word is uppercse!")
except Exception:
    print("Its just a Exception!")
finally:
    print("Code runned")