import psutil
import shutil

# CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Memory usage
memory = psutil.virtual_memory()
memory_used = memory.used / (1024 ** 3)
memory_total = memory.total / (1024 ** 3)
memory_percent = memory.percent

# Disk usage
disk = shutil.disk_usage("/")
disk_used = disk.used / (1024 ** 3)
disk_total = disk.total / (1024 ** 3)
disk_percent = (disk.used / disk.total) * 100

# Display results
print("---- System Resource Usage ----")
print(f"CPU Usage      : {cpu_usage}%")
print(f"Memory Usage   : {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_percent}%)")
print(f"Disk Usage     : {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent:.2f}%)")