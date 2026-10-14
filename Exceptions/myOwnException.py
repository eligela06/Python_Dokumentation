class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']

for word in words:
    if word.isupper():
        raise UppercaseException(word)