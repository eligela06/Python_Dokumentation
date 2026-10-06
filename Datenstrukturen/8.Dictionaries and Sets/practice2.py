import random
dictionary = {}
user_ids = []
user_id = 0
def new_id():
    global user_id
    while True:
        user_id = random.randint(1000,100000)
        if user_id in user_ids:
            continue
        else:
            user_ids.append(user_id)
            break

def new_user():
    global dictionary
    x = input("-name:")
    y = int(input("-age:"))

    new_id()
    dictionary[x]={"age":y,"ID":user_id}
    print("")

for i in range(10):
    new_user()

print(dictionary)

