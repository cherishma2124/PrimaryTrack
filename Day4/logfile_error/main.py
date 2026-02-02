error_lines = []
with open("app.log", "r") as logfile:
    for line in logfile:
        if "ERROR" in line:
            error_lines.append(line)
with open("error.log", "w") as errorfile:
    for error in error_lines:
        errorfile.write(error)

print("Error lines extracted successfully.")
