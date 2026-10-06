start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

print("\n8.11:")
for first, second in rhymes:

    for word in start1:
        print(word.capitalize() + "! ", end="")
    print(first.capitalize() + "!")


    print(start2 + " " + second + ".")