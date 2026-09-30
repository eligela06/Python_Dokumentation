scores = {"Ana": 92, "Ben": 67, "Cid": 81, "Dea": 55, "Eli": 74, "Fay": 40}
grades = {}
passing = {}
for score in scores:
    if scores[score] >= 90:
        grades[score] = "A"
    elif scores[score] >= 80:
        grades[score] = "B"
    elif scores[score] >= 70:
        grades[score] = "C"
    elif scores[score] >= 60:
        grades[score] = "D"
    else:
        grades[score] = "F"
    if scores[score] >= 60:
        passing[score] = grades[score]


print(grades, passing)