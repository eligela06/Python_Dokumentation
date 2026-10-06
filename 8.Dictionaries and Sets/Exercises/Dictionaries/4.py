# Deriving a new dictionary from another

# You are given a dictionary scores mapping student names to numeric scores:

# scores = {"Ana": 92, "Ben": 67, "Cid": 81, "Dea": 55, "Eli": 74, "Fay": 40}

# Build a grades dictionary mapping each name to a letter grade ("A" ≥ 90, "B" ≥ 80, "C" ≥ 70, "D" ≥ 60, else "F"). 
# Then build a second dictionary, passing, containing only students with a score of 60 or above.


scores = {"Ana": 92, "Ben": 67, "Cid": 81, "Dea": 55, "Eli": 74, "Fay": 40}
grades = dict(scores)
passing = dict()

for student, grade in grades.items():
    if grade >= 60:
        passing[student] = grade
    if grade >= 90:
        grades[student] = "A"
    elif grade >= 80:
        grades[student] = "B"
    elif grade >= 70:
        grades[student] = "C"
    elif grade >= 60:
        grades[student] = "D"
    else:
        grades[student] = "F"


print(grades)
print(passing)