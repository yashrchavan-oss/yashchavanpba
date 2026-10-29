import json

with open("employees.json", "r") as file:
    employees = json.load(file)

limit = float(input("Enter salary amount: "))

for emp in employees:
    if emp["salary"] > limit:
        print(emp)
[
    {"id": 1, "name": "Amit", "salary": 50000},
    {"id": 2, "name": "Priya", "salary": 70000},
    {"id": 3, "name": "Rahul", "salary": 40000}
]