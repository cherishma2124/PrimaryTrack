import os
import time
folder_path = "C:\\Users\\chari\\Desktop\\cleanup_folder"
days = 30
seconds = days * 24 * 60 * 60
now = time.time()
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isdir(file_path):
        continue
    file_time = os.path.getmtime(file_path)
    if now - file_time > seconds:
        os.remove(file_path)
        print(f"Deleted: {file}")
