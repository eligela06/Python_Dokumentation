s = input("--")
characters = {}

for character in s:
    characters[character] = characters.get(character, 0) + 1

print(characters)
