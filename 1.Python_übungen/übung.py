name = "elia".upper()
firstLetter = name[:1].upper()
name = name[1:]

name = firstLetter + name

print(name)
print(firstLetter)

secret = "The password is swordfish"

password = secret[16::]
password = "*"* len(password)

secret = secret[0:16] + password


print(secret)



quote = "There's no place like 127.0.0.1"
# Write expressions that determine:

# its length
# the first 7 characters
# the last 9 characters
# every second character
# the entire string backwards

print(len(quote))
print(quote[0:7])
print(quote[23:])
print(quote[0:-1:2])
print(quote[::-1])


sentence = "Python makes text manipulation surprisingly pleasant."

# gesucht = "pleasant."

# index = print(sentence.index(gesucht))
# länge = print(len(gesucht))
x1 = sentence[0:6]
x2 = sentence[44:53]
x3 = sentence[44:52]
print(x1,x2,x3)