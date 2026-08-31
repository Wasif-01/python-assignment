
marks = [
    [80, 75, 90],
    [65, 88, 70],
    [92, 78, 85],
    [55, 60, 72],
    [76, 95, 80]
]

maximum = marks[0][0]

for i in range(5):
    for j in range(3):
        if marks[i][j] > maximum:
            maximum = marks[i][j]

print("Maximum marks =", maximum)


minimum = marks[0][0]

for i in range(5):
    for j in range(3):
        if marks[i][j] < minimum:
            minimum = marks[i][j]

print("Minimum marks =", minimum)


total = 0

for i in range(5):
    for j in range(3):
        total = total + marks[i][j]

average = total / 15

print("Average marks =", average)


maximum_subject1 = marks[0][0]
student_id = 0

for i in range(1, 5):
    if marks[i][0] > maximum_subject1:
        maximum_subject1 = marks[i][0]
        student_id = i

print("Student ID =", student_id)
print("Maximum marks in Subject 1 =", maximum_subject1)



for j in range(3):
    subject_total = 0

    for i in range(5):
        subject_total = subject_total + marks[i][j]

    subject_average = subject_total / 5

    print("Average of Subject", j + 1, "=", subject_average)


    minimum = marks[][2]
    