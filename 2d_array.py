marks = [
    [80, 75, 90],   
    [65, 85, 70],  
    [90, 95, 88],   
    [55, 60, 65],   
    [72, 80, 78]    
]


maximum = max(max(row) for row in marks)
print("Maximum marks:", maximum)


minimum = min(min(row) for row in marks)
print("Minimum marks:", minimum)


total = sum(sum(row) for row in marks)
average = total / (5 * 3)
print("Average marks:", average)

subject_1 = [row[1] for row in marks]
max_marks_subject_1 = max(subject_1)

student_id = subject_1.index(max_marks_subject_1)

print("Maximum marks in subject 1:", max_marks_subject_1)
print("Student ID:", student_id)