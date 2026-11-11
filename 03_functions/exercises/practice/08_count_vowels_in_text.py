text = "Functions make programs easier to read"

def count_vowels(s):
    vowels = 0
    for letter in s.lower():
        if letter in ("a", "e", "i", "o", "u"):
            vowels += 1
    return vowels

print(count_vowels(text))
