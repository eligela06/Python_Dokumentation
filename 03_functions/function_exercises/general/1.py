def buggy(arg, result=[]):
    result.append(arg)
    print(result)



def works(arg):
    result=[]
    result.append(arg)
    print(result)

for i in range(2):
    buggy("a")
    works("b")