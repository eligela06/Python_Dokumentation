sentence = "the quick brown fox jumps over the lazy dog"
vowels = ("a","e","i","o","u")
vowels_in = {char for char in sentence if char in vowels}
print(vowels_in)