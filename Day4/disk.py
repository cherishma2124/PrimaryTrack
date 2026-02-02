import shutil
THRESHOLD = 80
disk = shutil.disk_usage("/")
total = disk.total / (1024 ** 3)
used = disk.used / (1024 ** 3)
free = disk.free / (1024 ** 3)
usage_percent = (disk.used / disk.total) * 100
print(f"Total Disk Space: {total:.2f} GB")
print(f"Used Disk Space: {used:.2f} GB")
print(f"Free Disk Space: {free:.2f} GB")
print(f"Disk Usage: {usage_percent:.2f}%")
if usage_percent > THRESHOLD:
    print(" WARNING: Disk usage exceeded threshold!")
else:
    print(" Disk usage is under control.")
