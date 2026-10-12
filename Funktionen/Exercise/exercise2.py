from functools import wraps




def document_it(func):
     def new_function(*args, **kwargs):
         print('Running function:', func.__name__)
         print('Positional arguments:', args)
         print('Keyword arguments:', kwargs)
         result = func(*args, **kwargs)
         print('Result:', result)
         return result
     return new_function


@document_it
def calc(num1,num2):
    return num1 * num2



calc(4,5)


def tst(str1,str2):
    @wraps
    def add(*args):
        pass
    return add

tst("Hallo","Elia")