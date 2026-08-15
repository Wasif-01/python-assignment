

employee = {
    "E1": {
        "emp_name": "Rahul",
        "designation": "Manager",
        "department": "HR",
        "salary": 60000
    },
    "E2": {
        "emp_name": "Amit",
        "designation": "Developer",
        "department": "IT",
        "salary": 75000
    },
    "E3": {
        "emp_name": "Asif",
        "designation": "Tester",
        "department": "IT",
        "salary": 55000
    },
    "E4": {
        "emp_name": "Wasif",
        "designation": "Accountant",
        "department": "Finance",
        "salary": 65000
    },
    "E5": {
        "emp_name": "Arjun",
        "designation": "Developer",
        "department": "IT",
        "salary": 90000
    }
}



print("1. Record of E1:")
print(employee["E1"])




print("\n2. Department of E4:")
print(employee["E4"]["department"])




max_salary = 0

for i in employee:
    if employee[i]["salary"] > max_salary:
        max_salary = employee[i]["salary"]
        max_id = i

print("\n3. Employee with maximum salary:")
print(employee[max_id])




employee["E6"] = {
    "emp_name": "Rajjak",
    "designation": "Designer",
    "department": "Design",
    "salary": 70000
}

print("\n4. Dictionary after inserting E6:")
print(employee)