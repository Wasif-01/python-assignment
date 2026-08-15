
student = {
    101: {
        "name": "Rahul",
        "department": "CSE",
        "marks": 85
    },
    102: {
        "name": "Priya",
        "department": "ECE",
        "marks": 92
    },
    103: {
        "name": "Amit",
        "department": "CSE",
        "marks": 78
    },
    104: {
        "name": "Sneha",
        "department": "IT",
        "marks": 88
    },
    105: {
        "name": "Rohan",
        "department": "EEE",
        "marks": 95
    }
}



sorted_students = dict(
    sorted(
        student.items(),
        key=lambda x: x[1]["marks"],
        reverse=True
    )
)

print("1. Students sorted by marks (High to Low):")
for roll, details in sorted_students.items():
    print(roll, details)



highest_student = max(
    student.items(),
    key=lambda x: x[1]["marks"]
)

print("\n2. Student with highest marks:")
print("Roll No:", highest_student[0])
print("Details:", highest_student[1])



average_marks = (
    lambda students:
    sum(map(lambda x: x["marks"], students.values()))
    / len(students)
)(student)

print("\n3. Average Marks:", average_marks)



above_average = dict(
    filter(
        lambda x: x[1]["marks"] > average_marks,
        student.items()
    )
)

print("\n4. Students scoring more than average marks:")
for roll, details in above_average.items():
    print("Roll No:", roll)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Marks:", details["marks"])
    print()