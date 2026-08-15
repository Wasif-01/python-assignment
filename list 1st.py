names = ["Rahul", "Asif", "Rohit", "Arindam", "Karan",
         "Vivek", "Aditya", "Wasif", "Raj", "Aman"]

marks = [85, 92, 76, 90, 65, 88, 79, 95, 70, 82]

max_index = marks.index(max(marks))
min_index = marks.index(min(marks))

print("Maximum marks:", marks[max_index])
print("Student:", names[max_index])

print("Minimum marks:", marks[min_index])
print("Student:", names[min_index])