employees = (
    "Rahul", "Amit", "Rohit", "Amit", "Karan",
    "Rahul", "Vivek", "Sahil", "Aman", "Rohit",
    "Amit", "Raj", "Karan", "Rahul", "Neha",
    "Vivek", "Amit", "Sahil", "Raj", "Rahul"
)

# 1. Print name and frequency
print("Employee name and frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))


# 2. Remove duplicate names
distinct_names = tuple(set(employees))

print("\nDistinct employee names:")
print(distinct_names)


# 3. Employee having maximum frequency
max_frequency = max(employees.count(name) for name in set(employees))

print("\nEmployee(s) having maximum frequency:")

for name in set(employees):
    if employees.count(name) == max_frequency:
        print(name, ":", max_frequency)


# 4. Sort tuple in alphabetical order
sorted_names = tuple(sorted(set(employees)))

print("\nEmployees in alphabetical order:")
print(sorted_names)


# 5. Search for a specific employee
search_name = input("\nEnter employee name to search: ")

if search_name in employees:
    print(search_name, "exists in the tuple")
else:
    print(search_name, "does not exist in the tuple")