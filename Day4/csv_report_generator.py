import csv
report_data = [
    ["ID", "Name", "Department", "Salary"],
    [1, "Alice", "IT", 50000],
    [2, "Bob", "HR", 40000],
    [3, "Charlie", "Finance", 45000]
]
with open("employee_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(report_data)
print("CSV report generated successfully.")