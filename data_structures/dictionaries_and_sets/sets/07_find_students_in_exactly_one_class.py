# Symmetric difference across 3+ sets

# You are given three sets representing class rosters:

# class_a = {"Tom", "Jerry", "Spike", "Tyke"}
# class_b = {"Jerry", "Tyke", "Butch"}
# class_c = {"Tom", "Butch", "Nibbles"}

# Find all students who appear in exactly one of the three classes (not two, not three). Careful: chaining the ^ operator pairwise across all three sets does not correctly generalize to "appears in exactly one of three or more sets" — think about why, and find an approach that gives the right answer.

class_a = {"Tom", "Jerry", "Spike", "Tyke","Elia"}
class_b = {"Jerry", "Tyke", "Butch"}
class_c = {"Tom", "Butch", "Nibbles"}

only_in_one = {
    student
    for student in class_a | class_b | class_c
    if sum(student in s for s in (class_a, class_b, class_c)) == 1
}

# only_in_one = class_a ^class_b^class_c

print(only_in_one)