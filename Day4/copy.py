with open("ip_addr_out.txt", "r") as file:
    with open("data.csv", "w") as fi:
        for line in file:
            fi.write(line)

print("File copied successfully.")