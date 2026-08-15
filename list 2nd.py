marks = [65, 78, 82, 55, 90, 72, 68, 85, 95, 60,
         75, 88, 92, 70, 64, 80, 58, 87, 73, 69]


average = sum(marks) / len(marks)
print("Average marks =", average)


count = 0

for i in marks:
    if i > average:
        count = count + 1

print("Students scoring more than average =", count)


maximum = max(marks)

print("Maximum score =", maximum)
print("Student index/position:")

for i in range(len(marks)):
    if marks[i] == maximum:
        print(i)