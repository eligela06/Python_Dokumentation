grades = {"Ann": [5, 4, 5], "Boris": [3, 4, 3], "Cathy": [5, 5, 5]}

def average(values):
    total = 0
    for element in values:
        total += element
    return total / len(values)

def best_student(data):
    highest_average = 0
    top_student = None
    for student, result in data.items():
        if average(result) > highest_average:
            highest_average = average(result)
            top_student = student

    return top_student

top_student = best_student(grades)
print("Best student:", top_student, "\nAverage:", average(grades[top_student]))