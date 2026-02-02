import re

log_file = "app.log"
pattern = r"ERROR\s+\d{4}-\d{2}-\d{2}\s+(\w+):\s+(.*)"

with open(log_file, "r") as file:
    for line_number, line in enumerate(file, start=1):
        match = re.search(pattern, line)
        if match:
            error_type = match.group(1)
            reason = match.group(2)

            print(f"Error found!")
            print(f"Line Number : {line_number}")
            print(f"Error Type  : {error_type}")
            print(f"Reason      : {reason}")
            print("-" * 40)
